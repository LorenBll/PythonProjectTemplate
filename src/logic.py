import threading
import time
import storage
# TODO : add module imports here



class Logic(threading.Thread):
    
    
    
    __storage = None
    # TODO : add class attributes here
    
    # ===== SETUP METHODS =====
    
    def __init__(self) -> None:
        """Initialise the logic layer."""
        
        # Call the Thread constructor
        super().__init__()
        
        # Start the storage layer
        self.__storage = storage.Storage()
        self.__storage.start()
        
        # TODO : initialisation code here
    
    
    
    # ===== LOGIC LAYER WORKING METHODS =====
    
    def run(self) -> None:
        """Run the logic layer."""
        
        # Check every 15 seconds that the storage layer still works
        while True:
            if not self.__storage.is_alive():
                # Restart the storage layer if it's not alive
                self.__storage = storage.Storage()
                self.__storage.start()
            time.sleep(15)
    
    def exit(self) -> None:
        """Exit the logic layer."""
        
        self.__storage.exit()
        
        # TODO : cleanup code here
    
    # TODO : add logic working methods here (all methods that compose the functioning of the application)
         


    # ===== EXPERIENCE LAYER > LOGIC LAYER METHODS =====

    # TODO : add experience layer > logic layer methods here (all methods that the experience layer calls)
