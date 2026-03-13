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

mouse_x = 0
mouse_y = 0

detail_toggle = True
detail_click_toggle = False


details = canvas.annotate('',(0,0),color='white',bbox = dict(facecolor='black',edgecolor='red',boxstyle='round,pad=0.5',alpha=0.5))
details_click = canvas.annotate('',(0,0),color='white',bbox = dict(facecolor='black',edgecolor='red',boxstyle='round,pad=0.5',alpha=0.5))

def on_key(event):
    global cursor_x
    global cursor_y
    global details
    global detail_toggle
    if event.key == 'up':
        cursor_y = max(0,cursor_y-1)
    elif event.key == 'down':
        cursor_y = min(image_y-1,cursor_y+1)
    elif event.key == 'left':
        cursor_x = max(0,cursor_x-1)
    elif event.key == 'right':
        cursor_x = min(image_x-1,cursor_x+1)
    elif event.key in {'h','H'}:
        detail_toggle = not detail_toggle
        details.set_visible(detail_toggle)
        details.set_text(f'x = {mouse_x}, y = {mouse_y}\nRGBA {img[mouse_y, mouse_x]*255}')
        details.set_position((mouse_x,mouse_y))
        window.canvas.draw_idle()
        return
    if(detail_click_toggle):
        cursor.set_data([[cursor_x], [cursor_y]])
        details_click.set_text(f'x = {cursor_x}, y = {cursor_y}\nRGBA {img[cursor_y, cursor_x]*255}')
        details_click.set_position((cursor_x,cursor_y))
        details_click.set_visible(True)
        window.canvas.draw_idle()

def on_click(event):
    global cursor_x_details
    global cursor_y_details
    global details_click
    global detail_click_toggle
    if event.button == 1:
        if event.inaxes:
            if not detail_click_toggle:
                cursor_x_details = int(event.xdata)
                cursor_y_details = int(event.ydata)
                cursor.set_visible(not cursor.get_visible())
                detail_click_toggle = not detail_click_toggle
                details_click.set_visible(detail_click_toggle)
            else:
                if abs(cursor_x_details - event.xdata) <= max(image_y//250,2) and abs(cursor_y_details - event.ydata) <= max(image_x//250,2):
                    cursor.set_visible(False)
                    details_click.set_visible(False)
                    detail_click_toggle = False
                    window.canvas.draw_idle()
                    return
                else:
                    cursor_x_details = int(event.xdata)
                    cursor_y_details = int(event.ydata)

    cursor.set_data([[cursor_x_details], [cursor_y_details]])
    details_click.set_text(f'x = {cursor_x}, y = {cursor_y}\nRGBA {img[cursor_y, cursor_x]*255}')
    details_click.set_position((cursor_x,cursor_y))
    details_click.set_visible(True)
    window.canvas.draw_idle()

def on_hover(event):
    global cursor_x
    global cursor_y
    global details
    global mouse_x
    global mouse_y
    if event.inaxes:
        mouse_x = int(event.xdata)
        mouse_y = int(event.ydata)
        if detail_toggle:
            cursor_x = int(event.xdata)
            cursor_y = int(event.ydata)
            details.set_text(f'x = {cursor_x}, y = {cursor_y}\nRGBA {img[cursor_y, cursor_x]*255}')
            details.set_position((cursor_x,cursor_y))
            details.set_visible(True)
        else:
            details.set_visible(False)
    window.canvas.draw_idle()

window.canvas.mpl_connect('key_press_event',on_key)
window.canvas.mpl_connect('button_press_event',on_click)
window.canvas.mpl_connect('motion_notify_event',on_hover)
pyplot.show()
