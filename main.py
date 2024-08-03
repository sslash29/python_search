import os
from pynput import keyboard
def search_function(array):
    current_input = []

    def clear_console():
        os.system('cls')

    def update():
        #! Keep at the top because we need to clear the console first then show the data if we put at the last line 
        #! of the function it will display the data then clear the console so we will have no way of seeing the data 
        #! because it's in a constant state of clearing the console
        clear_console()
        search_term = ''.join(current_input).lower()
        filtered_items = [item for item in array if search_term in item.lower()]
        print(f"Search term: {search_term}")
        print(f"Filtered items: {filtered_items}")

    def on_release(key):
        try:
            if key.char and key != keyboard.Key.backspace:
                current_input.append(key.char)
                update()
        except AttributeError:
            if key == keyboard.Key.enter:
                search_term = ''.join(current_input).lower()
                filtered_items = [item for item in array if search_term in item.lower()]
                if filtered_items:
                    print(f"Selected item: {filtered_items[0]}")
                    return False
                else:
                    print("No matching item found.")
                    return False
            elif key is keyboard.Key.backspace:
                if current_input:
                    current_input.pop(-1)
                    update()
            elif key == keyboard.Key.esc:
                return False
      

    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

array = [
    "item1",
    "item2",
    "item3",
    "ammar",
]

print(f"\nSearch for something in this array:\n{array}")
search_function(array=array)
