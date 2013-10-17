import sublime, sublime_plugin
import os

class JasmineCoffeeScriptDetectFileTypeCommand(sublime_plugin.EventListener):
  """ Detects current file type if the file's extension isn't conclusive """

  def on_load(self, view):
    filename = view.file_name()
    if not filename: # buffer has never been saved
      return

    name = os.path.basename(filename.lower())
    if name.endswith("spec.js.coffee") or name.endswith("spec.coffee"):
      set_syntax(view, "Jasmine CoffeeScript", "jasmine-coffeescript/Syntaxes")

def set_syntax(view, syntax, path=None):
  if path is None:
    path = syntax
  view.settings().set('syntax', 'Packages/'+ path + '/' + syntax + '.tmLanguage')
  print("Switched syntax to: " + syntax)
