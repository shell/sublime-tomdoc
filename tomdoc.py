import sublime_plugin
import re

class TomdocCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        point = self.view.sel()[0].end()
        line = self.read_line(point + 1)
        if not self.check_doc(point):
            return
        doc = self.compose_doc(line, edit)
        self.view.insert(edit, point, doc)

    def check_doc(self,point):
        current_line = self.read_line(point)
        params_match = re.search('#[ ]+Public |#[ ]+Examples |#[ ]+Returns |#', current_line)
        if not params_match:
            return True
        return False

    # Returns skeleton for initialize method
    def initialize_doc(self, params_match, current_line):
        indent = self.get_indent(current_line)
        lines = []
        lines.append(indent + "# Public: Initialize a Widget.")
        lines.append(indent + "#")
        params = [p.strip() for p in params_match.group(1).split(',') if len(p.strip()) > 0]
        for param in params:
          lines.append("%s# %s -" % (indent, param))
        return "\r\n" + "\r\n".join(lines)

    # Returns skeleton for initialize method
    def method_doc(self,params_match,current_line):
        params = [p.strip() for p in params_match.group(1).split(',') if len(p.strip()) > 0]
        indent = self.get_indent(current_line)
        lines = []
        lines.append(indent + "# Public: Duplicate some text an arbitrary number of times.")
        lines.append(indent + "#")
        for param in params:
          lines.append("%s# %s -" % (indent, param))
        if len(params) > 0:
          lines.append(indent + "#")
        lines.append(indent + "# Returns the duplicated String.")
        return "\r\n" + "\r\n".join(lines)


    # Returns skeleton for Class/Module
    def class_doc(self, params_match, current_line):
        indent = self.get_indent(current_line)
        lines = []
        lines.append(indent + "# Public: Various methods useful for performing mathematical operations.")
        lines.append(indent + "# All methods are module methods and should be called on the Math module.")
        lines.append(indent + "#")
        return "\r\n" + "\r\n".join(lines)

    # Returns skeleton for constant def
    # Example:
    #   # Public: Integer number of seconds to wait before connection timeout.
    def const_doc(self, params_match, current_line):
        indent = self.get_indent(current_line)
        lines = []
        lines.append(indent + "# Public: Integer number of seconds to wait before connection timeout.")
        return "\r\n" + "\r\n".join(lines)

    # Returns skeleton for attributes def
    # Example:
    #   attr_reader - # Public: Returns the String name of the user.
    #   attr_writer - # Public: Sets the String name of the user.
    #   attr_accessor - # Public: Gets/Sets the String name of the user.
    #   # Public: Returns the String name of the user.
    def attributes_doc(self, params_match, current_line):
        indent = self.get_indent(current_line)
        lines = []
        param = params_match.group(0).strip()
        if param == 'attr_reader':
            lines.append(indent + "# Public: Returns the String name of the user.")
        elif param == 'attr_writer':
            lines.append(indent + "# Public: Sets the String name of the user.")
        elif param == 'attr_accessor':
            lines.append(indent + "# Public: Gets/Sets the String name of the user.")
        return "\r\n" + "\r\n".join(lines)

    def compose_doc(self,current_line, edit):
        # Method definition
        params_match = re.search('def +[^ (]+[ (]*([^)]*)\)?', current_line)
        if params_match:
          if re.search('def initialize*', current_line):
            return self.initialize_doc(params_match, current_line)
          else:
            return self.method_doc(params_match, current_line)

        # Class/Module definition
        params_match = re.search('class | module', current_line)
        if params_match:
          return self.class_doc(params_match, current_line)

        # Constant definition definition
        params_match = re.search('[A-Z]+[ ]+=', current_line)
        if params_match:
          return self.const_doc(params_match, current_line)

        # Attributes definition
        # attr_reader, attr_writer, and attr_accessor
        params_match = re.search('attr_reader | attr_writer | attr_accessor ', current_line)
        if params_match:
          return self.attributes_doc(params_match, current_line)

    # Returns current indent
    def get_indent(self, line):
        return re.search('(^ *)', line).group(0)

    def read_line(self, point):
        if (point >= self.view.size()):
            return

        next_line = self.view.line(point)
        return self.view.substr(next_line)
