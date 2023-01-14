import platform
import sys
import eel

# Use latest version of Eel from parent directory
sys.path.insert(1, '../../')

def start_eel(develop):
    # Start Eel with either production or development configuration

    # Happens if `python index.py -dev` is used
    if develop:
        directory = 'src'
        page = {'port': 3000}
        arguments = dict(
            host='localhost',
        )

    # Happens if `python index.py` is used
    else:
        directory = 'build'
        page = 'index.html'
        arguments = dict(
            host='localhost', 
            port=8080,
        )

    # Initializes the directory we are going to use
    eel.init(directory)
    
    # Try to start the application using the page and arguments set above using chrome
    try :
        eel.start(page, **arguments)
    
    # If there is an error we try to use edge on a system that supports it
    except EnvironmentError:

        arguments = dict(
            mode='edge',
            host='localhost',
            port=8080,
        )

        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        if sys.platform in ['win32', 'win64'] and int(platform.release()) >= 10:
            eel.start(page, **arguments)
        else:
            raise



if __name__ == '__main__':
    # Call our start function and pass in wether or not we specified `-dev`
    start_eel(develop=len(sys.argv) == 2)
