import pywhatkit as pw

txt = '''Python offers numerous inbuilt libraries to ease our work. Among them pywhatkit is a Python library for sending WhatsApp messages at a certain time, it has several other features too.\n\n

Following are some features of pywhatkit module:\n\n

1)Send WhatsApp messages.\n
2)Play a YouTube video.\n
3)Perform a Google Search.\n
4)Get information on a particular topic.\n
The pywhatkit module can also be used for converting text into handwritten text images.'''

pw.text_to_handwriting(txt, "test.png", (0,0,138))
