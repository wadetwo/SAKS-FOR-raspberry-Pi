import entitis
from sakshat import SAKSHAT

SAKS=SAKSHAT()


if __name__ == "__main__":
    SAKS.digital_display.set_off()
    str = raw_input('input str to display:')
    SAKS.digital_display.show(str)
    
