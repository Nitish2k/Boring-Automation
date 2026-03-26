import can
import csv
from datetime import datetime

def log_can_data(interface='socketcan', channel='vcan0', duration=60, output_file='can_log.csv'):
    """
    Simple CAN data logging automation.
    
    Args:
        interface: CAN interface type (e.g., 'socketcan', 'kvaser', 'peak')
        channel: CAN channel name
        duration: Logging duration in seconds
        output_file: CSV file to save logs
    """
    
    # Initialize CAN bus
    bus = can.interface.Bus(channel=channel, interface=interface, bitrate=500000)
    
    # Open CSV file for writing
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'CAN ID', 'DLC', 'Data'])
        
        print(f"Logging CAN data for {duration} seconds...")
        start_time = datetime.now()
        
        try:
            while (datetime.now() - start_time).total_seconds() < duration:
                msg = bus.recv(timeout=1)
                
                if msg:
                    timestamp = datetime.now().isoformat()
                    can_id = hex(msg.arbitration_id)
                    dlc = msg.dlc
                    data = ' '.join([f'{byte:02X}' for byte in msg.data])
                    
                    writer.writerow([timestamp, can_id, dlc, data])
                    print(f"[{timestamp}] ID: {can_id} | Data: {data}")
        
        except KeyboardInterrupt:
            print("\nLogging stopped by user")
        finally:
            bus.shutdown()
    
    print(f"Log saved to {output_file}")

if __name__ == '__main__':
    log_can_data(duration=30)