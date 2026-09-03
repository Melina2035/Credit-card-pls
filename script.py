import PySimpleGUI as sg


sg.ChangeLookAndFeel("LightBlue")


right = [[sg.Text("H-hi there...")],
          [sg.Text("Do you th-think I could have your")],
          [sg.Text("credit card information, p-please?")],

          [
              sg.Text("Card number:"),
              sg.In(size=(25, 1), enable_events=True),
          ],
          [
              sg.Text("Expiry date:"),
              sg.In(size=(25, 1), enable_events=True),
          ],
          [
              sg.Text("Security code:"),
              sg.In(size=(25, 1), enable_events=True),
          ],

          [sg.Button("Th-thanks")],

          ]
left = [[sg.Image(filename="01.gif", subsample=3)],]

layout = [
    [
        sg.Column(left),
        sg.Column(right)
    ]
]

# Create the window
window = sg.Window(title="Totally Not Malware", layout=layout,margins=(10, 30), icon='0.ico')

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Th-thanks" or event == sg.WIN_CLOSED:
        break

window.close()