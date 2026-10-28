from pyfedappwrap.engine.runtime import FedDBEngine

from app import BiconApp

engine = FedDBEngine()
engine.register(BiconApp())

if __name__ == '__main__':
    engine.start()
    engine.wait_until_stop()
