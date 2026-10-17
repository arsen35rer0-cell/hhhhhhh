import os
import sys
from CMDSimulator import CMDSimulator

def main():
    # Очистка консоли
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 80)
    print("Microsoft Windows [Version 10.0.19045]".center(80))
    print("(c) Microsoft Corporation. All rights reserved.".center(80))
    print("=" * 80)
    print()
    
    simulator = CMDSimulator()
    simulator.run()

if __name__ == "__main__":
    main()
