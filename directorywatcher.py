import os
import time
import sendgrid

directory_to_watch = "/path/to/directory"

sg = sendgrid.SendGridClient('jch053', 'Shsu2013')

print "Currently Watching: " + directory_to_watch
before = dict([(f, None) for f in os.listdir (directory_to_watch)])
while 1:
    after = dict([(f, None) for f in os.listdir(directory_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if removed:
        print "Removed: ", ", ".join(removed)
        message = sendgrid.Mail()
        message.add_to('Jaken Herman <JakenHerman7@Gmail.com>')
        message.set_subject('Directory Changes')
        message.set_text('Something has been removed from your directory')
        message.set_from('Jaken Herman <jch053@shsu.edu>')
        status, msg = sg.send(message)
    if added:
       print "Added: ", ", ".join(added)
       message = sendgrid.Mail()
       message.add_to('Jaken Herman <JakenHerman7@Gmail.com>')
       message.set_subject('Directory Changes')
       message.set_text('Something has been added to your directory')
       message.set_from('Jaken Herman <jch053@shsu.edu>')
       status, msg = sg.send(message)
    time.sleep(5)
    before = after
