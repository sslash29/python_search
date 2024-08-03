from pynput import keyboard

def search_function(array):
    current_input = []

    def update_search():
        search_term = ''.join(current_input).lower()
        filtered_items = [item for item in array if search_term in item.lower()]
        print(f"Search term: {search_term}")
        print(f"Filtered items: {filtered_items}")

    def on_press(key):
        try:
            if key.char and key != keyboard.Key.backspace:
                current_input.append(key.char)
                update_search()
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
            elif key == keyboard.Key.backspace:
                if current_input:
                    current_input.pop()
                    update_search()
            else:
                print(f'Special key pressed: {key}')

    def on_release(key):
        if key == keyboard.Key.esc:
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

array = [
    "item1",
    "item2",
    "item3",
    "ammar",
]

print(f"Search for something in this array:\n{array}")
search_function(array=array)
