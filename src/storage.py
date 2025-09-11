import threading
import time
# TODO : add module imports here



class Storage(threading.Thread):
    
    
    
    # TODO : add class attributes here
    
    # ===== SETUP METHODS =====
    
    def __init__(self) -> None:
        """Initialise the storage layer."""
        
        # Call the Thread constructor
        super().__init__()
        
        # TODO : initialisation code here
        
        pass
    


    # ===== STORAGE LAYER WORKING METHODS =====

    def run(self) -> None:
        """Run the storage layer."""
        
        # Check every 15 seconds that the data is still accessible
        while True:
            if not self.isDataAccessible():
                # TODO : add code to handle inaccessible data here
                pass
            time.sleep(15)

    def exit(self) -> None:
        """Exit the storage layer."""
        
        # TODO : add cleanup code here
        
        pass

    def isDataAccessible(self) -> bool:
        """Check if the data is accessible."""
        # TODO : add code to check data accessibility here
        return True

    # TODO : add storage layer working methods here (all methods that compose the storage of the application)



    # ===== LOGIC LAYER > STORAGE LAYER METHODS =====

    # TODO : add logic layer > storage layer methods here (all methods that the logic layer calls)
