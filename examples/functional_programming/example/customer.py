from dataclasses import dataclass

@dataclass(frozen=True)
class Customer():
    name: str
    address: str
    enterprise: bool

    @staticmethod
    def notify(cust, msg):
        print(f'Sending {msg} to {cust.name} at {cust.address}')        
        