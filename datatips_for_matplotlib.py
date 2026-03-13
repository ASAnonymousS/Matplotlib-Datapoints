from matplotlib import pyplot

img_location = input('Enter the location of the image:\n')
img_name = input('What do you want the image to be called ?\n')

img = pyplot.imread(img_location)

image_y, image_x, channel = img.shape

window, canvas = pyplot.subplots()
canvas.imshow(img)
canvas.set_title(f"{img_name}'s Resolution = {image_x} x {image_y}")


cursor,*_ = canvas.plot(0, 0, 'r+', markersize = 25, markeredgewidth = 2, visible = False)
cursor_x = cursor.get_xdata()[0]
cursor_y = cursor.get_ydata()[0]


details = canvas.annotate('',(0,0))
details_click = canvas.annotate('',(0,0))

def on_key(event):
    global cursor_x
    global cursor_y
    global details
    if event.key == 'up':
        cursor_y = max(0,cursor_y-1)
    elif event.key == 'down':
        cursor_y = min(image_y-1,cursor_y+1)
    elif event.key == 'left':
        cursor_x = max(0,cursor_x-1)
    elif event.key == 'right':
        cursor_x = min(image_x-1,cursor_x+1)
    elif event.key in {'h','H'}:
        cursor.set_visible(False)
        try:
            details.remove()
        except:
            pass
        window.canvas.draw_idle()
        return
    cursor.set_data([[cursor_x], [cursor_y]])
    try:
        details.remove()
    except:
        pass
    details = canvas.annotate(f'x = {cursor_x}, y = {cursor_y}\nRGBA {img[cursor_y, cursor_x]*255}',(cursor_x, cursor_y),color='white',bbox = dict(facecolor='black',edgecolor='red',boxstyle='round,pad=0.5',alpha=0.5))
    window.canvas.draw_idle()

def on_click(event):
    global cursor_x_details
    global cursor_y_details
    global details_click
    if event.button == 1:
        if event.inaxes:
            if not cursor.get_visible():
                cursor_x_details = int(event.xdata)
                cursor_y_details = int(event.ydata)
                cursor.set_visible(not cursor.get_visible())
            else:
                if abs(cursor_x_details - event.xdata) <= image_y//250 and abs(cursor_y_details - event.ydata) <= image_x//250:
                    cursor.set_visible(False)
                    try:
                        details_click.remove()
                    except:
                        pass
                    window.canvas.draw_idle()
                    return
                else:
                    cursor_x_details = int(event.xdata)
                    cursor_y_details = int(event.ydata)

    cursor.set_data([[cursor_x_details], [cursor_y_details]])
    try:
        details_click.remove()
    except:
        pass
    details_click = canvas.annotate(f'x = {cursor_x_details}, y = {cursor_y_details}\nRGBA {img[cursor_y_details, cursor_x_details]*255}',(cursor_x_details, cursor_y_details),color='white',bbox = dict(facecolor='black',edgecolor='red',boxstyle='round,pad=0.5',alpha=0.5))
    window.canvas.draw_idle()

def on_hover(event):
    global cursor_x
    global cursor_y
    global details
    if event.inaxes:
        cursor_x = int(event.xdata)
        cursor_y = int(event.ydata)
        try:
            details.remove()
        except:
            pass
        details = canvas.annotate(f'x = {cursor_x}, y = {cursor_y}\nRGBA {img[cursor_y, cursor_x]*255}',(cursor_x, cursor_y),color='white',bbox = dict(facecolor='black',edgecolor='red',boxstyle='round,pad=0.5',alpha=0.5))
    else:
        try:
            details.remove()
        except:
            pass
    window.canvas.draw_idle()

window.canvas.mpl_connect('key_press_event',on_key)
window.canvas.mpl_connect('button_press_event',on_click)
window.canvas.mpl_connect('motion_notify_event',on_hover)
pyplot.show()
