from aqt import mw
from aqt.qt import QAction

from .config import conf

def setupMenu() -> None:
    menu = mw.form.menuTools
    a = QAction("ReColor Settings", menu)
    a.triggered.connect(conf.open_config)
    menu.addAction(a)


setupMenu()
