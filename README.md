## SublimeText package for generating TomDoc

[TomDoc](http://tomdoc.org/)

### Installation

### Without package manager

Go to your Sublime Text 2 Packages directory and clone the repository using the command below:

    git clone git@github.com:shell/sublime-tomdoc.git

Don't forget to keep updating it, though!

### Usage

Pressing **ctrl+enter** on the previous line of method definition

    def hello a, b
    end

results

    # Public: Duplicate some text an arbitrary number of times.
    #
    # a -
    # b -
    #
    # Returns the duplicated String.    
    def hello a, b

    end
    
Works respectfully for all other supported constructions   

Type 'tom' and hit **TAB** to generate default TomDoc skeleton text.

Support following constructions for TomDoc:     

  * Method Documentation
  * Initialize method Documentation
  * Class/Module Documentation
  * Constants Documentation
  * Attributes
  

### Author

Vladimir Penkin

Credits to:                   

  * [Revath S Kumar](https://github.com/revathskumar/sublime-yardoc)
  * [Brandon Hilkert](https://github.com/brandonhilkert/tomdoc-sublime)

Please see [licence](http://github.com/shell/sublime-tomdoc/blob/master/LICENSE)

