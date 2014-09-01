import os, time
import tempfile


# taken from http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html
# In case of Poprocorn Time we have to watch for the creating of %TEMP%\Popcorn Time folder and then list
# the movie folders under it

path_to_watch = tempfile.gettempdir()
print "Monitoring folder: %s" % path_to_watch

before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (10)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added: print "Added: ", ", ".join (added)
  if removed: print "Removed: ", ", ".join (removed)
  before = after
