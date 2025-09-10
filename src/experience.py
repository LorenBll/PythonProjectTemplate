import threading
import logic
# TODO : add module imports here



class Experience(threading.Thread):
    
    
    
    __logic = None
    # TODO : add class attributes here
    
    # ===== SETUP METHODS =====
    
    def __init__(self) -> None:
        """Initialise the experience layer."""
        
        # Call the Thread constructor
        super().__init__()

        self.__logic = logic.Logic()
        self.__logic.start()

        # TODO : initialisation code here
        
        pass
    
    
    
    # ===== EXPERIENCE LAYER WORKING METHODS =====
    
    def run(self) -> None:
        """Run the experience layer."""
        
        # TODO : experience layer running code here
        
        pass
    
    # TODO : add experience layer working methods here (all methods that compose the functioning of the experience layer)
    

def main() -> None:
    experience = Experience()
    experience.start()
    
if __name__ == "__main__":
    main()