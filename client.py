# -*- coding: utf-8 -*-
"""Bebsi — клиент v7.2: ответы, правки, удаление, пересылка, избранное, файлы,
реакции и копирование правой кнопкой."""

import sys
try:
    try:
        try:
            import faulthandler
        except Exception:
            faulthandler = None
    except Exception:
        faulthandler = None
except Exception:
    faulthandler = None
import os
def _bebsi_excepthook(t, v, tb):
    import traceback
    msg = "".join(traceback.format_exception(t, v, tb))
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "crash.log"), "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass
    try:
        import ctypes
        ctypes.windll.user32.MessageBoxW(0, msg[:1800], "Bebsi — crash", 0x10)
    except Exception:
        pass
sys.excepthook = _bebsi_excepthook
if sys.stderr is None or sys.stdout is None:
    class _WinLog:
        def __init__(self, p):
            self.f = open(p, "a", encoding="utf-8", buffering=1)
        def write(self, s):
            try:
                self.f.write(s)
            except Exception:
                pass
        def flush(self):
            try:
                self.f.flush()
            except Exception:
                pass
        def isatty(self):
            return False
        def fileno(self):
            return self.f.fileno()
    _lp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bebsi_windowed.log")
    if sys.stderr is None:
        sys.stderr = _WinLog(_lp)
    if sys.stdout is None:
        sys.stdout = _WinLog(_lp)
if getattr(sys, "frozen", False):
    CLIENT_PATH = os.path.join(os.path.dirname(sys.executable), "client.py")
else:
    CLIENT_PATH = os.path.abspath(__file__)
if getattr(sys, "frozen", False):
    for _k in [k for k in os.environ if ("MEIPASS" in k.upper()) or ("PYI" in k.upper())]:
        os.environ.pop(_k, None)
def _upd_dbg(msg):
    return
    try:
        import datetime
        p = os.path.join(os.path.dirname(CLIENT_PATH), "update_debug.log")
        with open(p, "a", encoding="utf-8") as f:
            f.write(f"{datetime.datetime.now():%H:%M:%S} {msg}\n")
    except Exception:
        pass
# --- BEBSI_SAFE_RESTART_v2 ---
if getattr(sys, "frozen", False):
    import subprocess as _sp
    _EXE = os.path.abspath(sys.executable)
    def _is_self(cmd):
        try:
            return os.path.normcase(os.path.abspath(str(cmd).split()[0].strip('"'))) == os.path.normcase(_EXE)
        except Exception:
            return False
    def _mk_bat():
        bat = os.path.join(os.path.dirname(_EXE), "_restart.bat")
        with open(bat, "w") as f:
            f.write('@echo off\r\ntimeout /t 2 /nobreak >nul\r\nstart "" "' + _EXE + '"\r\ndel "%~f0"\r\n')
        return bat
    _orig_popen = _sp.Popen
    def _do_self_restart():
        _upd_dbg("RESTART через бат из СВЕЖЕГО процесса")
        try:
            env = {k: v for k, v in os.environ.items() if k != "_MEIPASS2"}
            _orig_popen(["cmd", "/c", _mk_bat()], env=env, creationflags=0x08000000)
        except Exception:
            pass
        pass
    class _SafePopen(_orig_popen):
        def __init__(self, args, *a, **kw):
            try:
                c0 = args[0] if isinstance(args, (list, tuple)) else str(args)
                if _is_self(c0):
                    _do_self_restart()
            except Exception:
                pass
            super().__init__(args, *a, **kw)
    _sp.Popen = _SafePopen
    _orig_run = _sp.run
    def _run(args, *a, **kw):
        try:
            c0 = args[0] if isinstance(args, (list, tuple)) else str(args)
            if _is_self(c0):
                _do_self_restart()
        except Exception:
            pass
        return _orig_run(args, *a, **kw)
    _sp.run = _run
    _orig_call = _sp.call
    def _call(args, *a, **kw):
        try:
            c0 = args[0] if isinstance(args, (list, tuple)) else str(args)
            if _is_self(c0):
                _do_self_restart()
        except Exception:
            pass
        return _orig_call(args, *a, **kw)
    _sp.call = _call
    _orig_execv = os.execv
    def _execv(path, args):
        if _is_self(path):
            _do_self_restart()
        return _orig_execv(path, args)
    os.execv = _execv
    _orig_system = os.system
    def _system(cmd):
        if _is_self(cmd):
            _do_self_restart()
        return _orig_system(cmd)
    os.system = _system
    try:
        from PySide6.QtCore import QProcess
        _orig_qstart = QProcess.start
        def _qstart(self, *a, **kw):
            try:
                prog = a[0] if a else self.program()
                if _is_self(prog):
                    _do_self_restart()
            except Exception:
                pass
            return _orig_qstart(self, *a, **kw)
        QProcess.start = _qstart
    except Exception:
        pass
    _orig_startfile = os.startfile
    def _startfile(path, *a, **kw):
        if _is_self(path):
            _do_self_restart()
        return _orig_startfile(path, *a, **kw)
    os.startfile = _startfile
# --- END BEBSI_SAFE_RESTART_v2 ---
_upd_dbg("BOOT frozen=%s path=%s" % (getattr(sys, "frozen", False), CLIENT_PATH))
try:
    import hashlib as _hl0
    OWN_HASH = _hl0.sha256(open(__file__, "rb").read()).hexdigest()
except Exception:
    OWN_HASH = ""

import os
import time

import os
import io
import json
import re
import time
import wave
import base64
import socket
import hashlib
import tempfile
import math
import random
import subprocess
from datetime import datetime

import os
import time


from PySide6.QtCore import (QObject, QEvent, Qt, Signal, QThread, QTimer, QPoint, QPointF, QSize, QByteArray,


                            QBuffer, QIODevice, QUrl, QPropertyAnimation, QParallelAnimationGroup,
                            QSequentialAnimationGroup, QPauseAnimation, QEasingCurve)
from PySide6.QtGui import (QColor, QPainter, QPainterPath, QLinearGradient, QRadialGradient, QBrush, QPen,


                           QPalette, QImage, QPixmap, QRegion, QCursor, QIcon, QDesktopServices)
from PySide6.QtWidgets import (QApplication, QWidget, QFrame, QLabel, QLineEdit, QPushButton, QStyle,


                               QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget, QScrollArea,
                               QGraphicsOpacityEffect, QGraphicsDropShadowEffect, QFileDialog, QDialog, QMenu, QComboBox, QSystemTrayIcon,
                               QListWidget, QListWidgetItem, QInputDialog, QTabWidget)
from PySide6.QtWidgets import QCheckBox
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect


from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QCheckBox



# ================== НАСТРОЙКИ ==================
APP_NAME = "Bebsi"
APP_SUBTITLE = "Через тернии к звёздам"
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9100
if getattr(sys, "frozen", False):
    if getattr(sys, "frozen", False):
        if getattr(sys, "frozen", False):
            DIR = os.path.dirname(os.path.abspath(sys.executable))
        else:
            DIR = os.path.dirname(os.path.abspath(__file__))
    else:
        DIR = os.path.dirname(os.path.abspath(__file__))
else:
    DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(DIR, "settings.json")
MODEL_PATH = os.path.join(DIR, "model_ru")

EMOJIS = ["😀","😁","😂","🤣","😊","😍","😘","😎","🤔","🙃","😢","😭","😡","🥳","🥺","😴","","🤩","","😈","\U0001F44D","👎","\U0001F64F","👏","💪","🤙","️","🤝","","❤️","💔","💯","\U0001F525","⭐","⚡","🌚","🌝","🌈","🌙","☀️","","🍔","","🎂","","⚽","🏆","🚀","🎮","🎵","🌸","🫶","💫","😇","🤡",""]
EMOJI_NAMES = {"fire": "🔥", "heart": "❤️", "smile": "😀", "laugh": "😂", "cry": "😢", "angry": "😡", "cool": "😎", "think": "🤔", "kiss": "😘", "wink": "😉", "party": "🥳", "sad": "😭", "sleep": "😴", "ok": "👌", "star": "⭐", "zap": "⚡", "moon": "🌙", "sun": "☀️", "cat": "🐱", "dog": "🐶", "music": "🎵", "game": "🎮", "rocket": "🚀"}
REACTIONS = ["❤️", "\U0001F44D", "\U0001F525", "😂", "😮", "😢"]

THEMES = {
    "Тёмная": {'bg': '#0b0e1a', 'bg2': '#10142a', 'text': '#eef0ff', 'muted': '#a6abcd', 'accent': '#7c5cff', 'accent2': '#22d3ee', 'bubbleMine': '#7c5cff', 'bubbleOther': '#161a2e', 'stroke': '#262b45', 'input': '#141830', 'hover': '#1b2038', 'panel': '#0e1224', 'side': '#0e1224', 'card': '#151a30', 'border': '#262b45', 'bubble': '#161a2e', 'online': '#34d399', 'warn': '#fbbf24', 'err': '#fb7185', 'sel': '#232a4d', 'btn': '#1b2038', 'title': '#eef0ff', 'messages': '#151a30', 'avatar': '#151a30', 'group': '#151a30', 'stories': '#151a30', 'bio': '#151a30', 'display': '#151a30', 'groups': '#151a30', 'users': '#151a30', 'id': '#151a30', 'votes': '#151a30', 'ttl': '#151a30', 'msg_id': '#151a30', 'caption': '#151a30', 'ts': '#151a30', 'from': '#151a30', 'peer': '#151a30', 'data': '#151a30', 'user': '#151a30', 'type': '#151a30', 'media': '#151a30', 'reactions': '#151a30', 'username': '#151a30'},
    "Светлая": {'bg': '#f6f7ff', 'bg2': '#ffffff', 'text': '#171a2e', 'muted': '#54596f', 'accent': '#6d4dff', 'accent2': '#06b6d4', 'bubbleMine': '#6d4dff', 'bubbleOther': '#ffffff', 'stroke': '#e3e6f6', 'input': '#ffffff', 'hover': '#eef0fb', 'panel': '#fbfcff', 'side': '#fbfcff', 'card': '#ffffff', 'border': '#e3e6f6', 'bubble': '#ffffff', 'online': '#10b981', 'warn': '#d97706', 'err': '#e11d48', 'sel': '#e6e9ff', 'btn': '#eef0fb', 'title': '#171a2e', 'messages': '#ffffff', 'avatar': '#ffffff', 'group': '#ffffff', 'stories': '#ffffff', 'bio': '#ffffff', 'display': '#ffffff', 'groups': '#ffffff', 'users': '#ffffff', 'id': '#ffffff', 'votes': '#ffffff', 'ttl': '#ffffff', 'msg_id': '#ffffff', 'caption': '#ffffff', 'ts': '#ffffff', 'from': '#ffffff', 'peer': '#ffffff', 'data': '#ffffff', 'user': '#ffffff', 'type': '#ffffff', 'media': '#ffffff', 'reactions': '#ffffff', 'username': '#ffffff'},
}
WALLPAPERS = ["Классика", "Градиент", "Горошек", "Звёзды", "Закат", "Океан", "Сакура"]
CUR = dict(THEMES["Тёмная"])
WALL = "Классика"
MIC_DEV = -1
CAM_DEV = 0
TTLS = {}
ACCOUNTS = []
SAVED = {}
LAST_U = ""
LOCK_HASH = ""
VOSK_MODEL = None
SOUND_ON = True
TOASTS_ON = True


def load_settings():
    global CUR, WALL, MIC_DEV, CAM_DEV, TTLS, ACCOUNTS, SAVED, LAST_U, LOCK_HASH, SOUND_ON, TOASTS_ON
    try:
        with open(SETTINGS_PATH, encoding="utf-8") as f:
            s = json.load(f)
        CUR = dict(THEMES.get(s.get("theme", "Тёмная"), THEMES["Тёмная"]))
        WALL = s.get("wallpaper", "Классика")
        if WALL not in WALLPAPERS:
            WALL = "Классика"
        MIC_DEV = int(s.get("mic", -1))
        CAM_DEV = int(s.get("cam", 0))
        TTLS = s.get("ttls", {})
        ACCOUNTS = s.get("accounts", [])
        LAST_U = s.get("last", "")
        SAVED = s.get("saved_notes", {})
        LOCK_HASH = s.get("lock", "")
        SOUND_ON = bool(s.get("sound", True))
        TOASTS_ON = bool(s.get("toasts", True))
        _seen = set()
        _clean = []
        for _a in ACCOUNTS:
            if isinstance(_a, dict) and _a.get("u") and _a["u"] not in _seen:
                _seen.add(_a["u"])
                _clean.append(_a)
        ACCOUNTS[:] = _clean[:3]
        _mig = False
        for _a in ACCOUNTS:
            _p = _a.get("p", "") or ""
            if _p and not _p.startswith("dpapi:"):
                _e = _dpapi_protect(_p.encode("utf-8"))
                if _e:
                    _a["p"] = _e
                    _mig = True
        if _mig:
            save_settings()
    except Exception:
        pass


def save_settings():
    try:
        name = next((k for k, v in THEMES.items() if v == CUR), "Тёмная")
        with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
            json.dump({"theme": name, "wallpaper": WALL, "mic": MIC_DEV, "cam": CAM_DEV, "ttls": TTLS, "accounts": ACCOUNTS, "last": LAST_U, "saved_notes": SAVED, "lock": LOCK_HASH, "sound": SOUND_ON, "toasts": TOASTS_ON, "sched": SCHED}, f, ensure_ascii=False)
    except Exception:
        pass


def _dpapi_protect(b):
    try:
        import ctypes, ctypes.wintypes as wt
        class _D(ctypes.Structure):
            _fields_ = [("cb", wt.DWORD), ("pb", ctypes.POINTER(ctypes.c_ubyte))]
        inp = _D(len(b), (ctypes.c_ubyte * len(b)).from_buffer_copy(b))
        out = _D()
        if ctypes.windll.crypt32.CryptProtectData(ctypes.byref(inp), None, None, None, None, 0, ctypes.byref(out)):
            data = ctypes.string_at(out.pb, out.cb)
            ctypes.windll.kernel32.LocalFree(out.pb)
            return "dpapi:" + base64.b64encode(data).decode()
    except Exception:
        pass
    return ""
def _dpapi_unprotect(s):
    try:
        if not str(s).startswith("dpapi:"):
            return ""
        raw = base64.b64decode(str(s)[6:])
        import ctypes, ctypes.wintypes as wt
        class _D(ctypes.Structure):
            _fields_ = [("cb", wt.DWORD), ("pb", ctypes.POINTER(ctypes.c_ubyte))]
        inp = _D(len(raw), (ctypes.c_ubyte * len(raw)).from_buffer_copy(raw))
        out = _D()
        if ctypes.windll.crypt32.CryptUnprotectData(ctypes.byref(inp), None, None, None, None, 0, ctypes.byref(out)):
            data = ctypes.string_at(out.pb, out.cb)
            ctypes.windll.kernel32.LocalFree(out.pb)
            return data.decode("utf-8", "ignore")
    except Exception:
        pass
    return ""
def acc_pw(a):
    p = a.get("p", "") or ""
    return _dpapi_unprotect(p) or p

def lock_hash(code):
    return hashlib.sha256(("bebsi-lock:" + (code or "")).encode()).hexdigest()

def dnd_active():
 if not DND_ON:
  return False
 h = datetime.now().hour
 if DND_FROM <= DND_TO:
  return DND_FROM <= h < DND_TO
 return h >= DND_FROM or h < DND_TO

def rgba(h, a):
    h = h.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return f"rgba({r},{g},{b},{a})"

def _meta_color(mine):
    return "rgba(255,255,255,175)" if mine else rgba(CUR['muted'], 235)
def _is_light():
    try:
        return QColor(CUR["bg"]).lightness() > 140
    except Exception:
        return False
def _device_name():
    try:
        import platform
        return platform.node() or "ПК"
    except Exception:
        return "ПК"

def _fmt_ts(ts):
    try:
        return datetime.fromtimestamp(float(ts or 0)).strftime("%d.%m.%y %H:%M")
    except Exception:
        return "—"



_orig_dlg_exec = QDialog.exec
def _styled_exec(self, *a, **k):
    try:
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setObjectName("dlg")
        from PySide6.QtWidgets import QShortcut
        from PySide6.QtGui import QKeySequence
        QShortcut(QKeySequence("Esc"), self).activated.connect(self.reject)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        _bg = rgba(CUR.get("card", "#1e1e28"), 252)
        _bd = rgba(CUR.get("stroke", "#2a2a36"), 180)
        self.setStyleSheet("QDialog#dlg { background: " + _bg + "; border-radius: 16px; border: 1px solid " + _bd + "; }")
    except Exception:
        pass
    return _orig_dlg_exec(self, *a, **k)
QDialog.exec = _styled_exec

def build_qss(t):
    return f"""
    #dlg {{ background: {rgba(t['panel'], 250)}; border-radius: 16px; border: 1px solid {rgba(t['stroke'], 140)}; }}
* {{ outline: none; }}
QWidget {{ background: transparent; color: {t["text"]}; font-family: "Segoe UI Variable Display", "Segoe UI", "SF Pro Display", "Helvetica Neue", Arial, sans-serif; }}
QStackedWidget {{ background: transparent; }}
QLineEdit {{ background: {rgba(t["input"], 200)}; border: 1px solid {rgba(t["stroke"], 200)}; border-radius: 14px; padding: 11px 16px; font-size: 14px; selection-background-color: {t["accent"]}; }}
QLineEdit:focus {{ border: 1px solid {t["accent"]}; background: {rgba(t["input"], 235)}; }}
QPushButton {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 {t["accent"]}, stop:1 {t["accent2"]}); border: none; border-radius: 14px; padding: 11px 20px; font-size: 14px; font-weight: 700; color: #ffffff; }}
QPushButton:hover {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 {t["accent2"]}, stop:1 {t["accent"]}); }}
QPushButton:pressed {{ background: {t["accent"]}; }}
#ghostBtn {{ background: {rgba(t["hover"], 120)}; color: {t["muted"]}; font-weight: 600; padding: 8px 14px; border: 1px solid {rgba(t["stroke"], 160)}; }}
#ghostBtn:hover {{ background: {rgba(t["hover"], 220)}; color: {t["text"]}; border: 1px solid {rgba(t["accent"], 120)}; }}
#closeBtn {{ background: {rgba(t["hover"], 200)}; color: {t["text"]}; font-size: 18px; font-weight: 700; border-radius: 12px; padding: 0; }}
#closeBtn:hover {{ background: {t["err"]}; color: #ffffff; }}
#toolBtn {{ background: {rgba(t["bubble"], 200)}; border: 1px solid {rgba(t["stroke"], 200)}; border-radius: 12px; font-size: 16px; padding: 0; }}
#toolBtn:hover {{ background: {rgba(t["accent"], 60)}; border: 1px solid {rgba(t["accent"], 140)}; }}
#emojiBtn {{ background: transparent; border: none; font-size: 22px; padding: 0; }}
#emojiBtn:hover {{ background: {rgba(t["hover"], 200)}; border-radius: 12px; }}
#chipBtn {{ background: {rgba(t["bubble"], 200)}; border: 1px solid {rgba(t["stroke"], 200)}; border-radius: 10px; padding: 3px 8px; font-size: 12px; color: {t["text"]}; }}
#chipBtn[mine="true"] {{ border: 1px solid {t["accent"]}; }}
#card {{ background: {rgba(t["card"], 235)}; border: 1px solid {rgba(t["stroke"], 160)}; border-radius: 28px; }}
#title {{ font-size: 26px; font-weight: 800; letter-spacing: 0.5px; }}
#subtitle {{ color: {t["muted"]}; font-size: 13px; }}
#sidebar {{ background: {rgba(t["panel"], 190)}; border-right: 1px solid {rgba(t["stroke"], 220)}; }}
#chatItem {{ border-radius: 16px; }}
#chatItem:hover {{ background: {rgba(t["hover"], 160)}; }}
#chatItem[selected="true"] {{ background: {rgba(t["accent"], 40)}; border: 1px solid {rgba(t["accent"], 120)}; }}
#itemName {{ font-size: 14px; font-weight: 600; }}
#itemLast {{ color: {t["muted"]}; font-size: 12px; }}
#itemTime {{ color: {t["muted"]}; font-size: 10px; }}
#badge {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 #ff5e7d, stop:1 #ff9e7d); color: #fff; border-radius: 10px; font-size: 10px; font-weight: 800; padding: 2px 7px; }}
#chatHeader {{ background: {rgba(t["panel"], 120)}; border-bottom: 1px solid {rgba(t["stroke"], 120)}; }}
#peerName {{ font-size: 16px; font-weight: 700; }}
#statusLbl {{ font-size: 12px; color: {t["muted"]}; }}
#bubbleMine {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 {t["accent"]}, stop:1 {t["accent2"]}); border-radius: 20px; border-bottom-right-radius: 6px; }}
#bubbleOther {{ background: {rgba(t["bubble"], 200)}; border: 1px solid {rgba(t["stroke"], 160)}; border-radius: 20px; border-bottom-left-radius: 6px; }}
#msgInput {{ background: {rgba(t["card"], 160)}; border: 1px solid {rgba(t["stroke"], 200)}; border-radius: 20px; padding: 10px 16px; font-size: 14px; }}
#msgInput:focus {{ border: 1px solid {t["accent"]}; background: {rgba(t["card"], 220)}; }}
#sendBtn {{ border-radius: 20px; font-size: 15px; padding: 0; }}
#sendBtn:hover {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 {t["accent2"]}, stop:1 {t["accent"]}); }}
#emptyLbl {{ color: {t["muted"]}; font-size: 14px; }}
#banner {{ background: {rgba(t["hover"], 200)}; border-left: 3px solid {t["accent"]}; border-radius: 14px; }}
QDialog {{ background: {rgba(t["card"], 240)}; }}
    #setRow {{ background: {rgba(t['bubble'], 200)}; border: 1px solid {rgba(t['stroke'], 200)}; border-radius: 12px; }}
    #setRow:hover {{ background: {rgba(t['hover'], 220)}; border: 1px solid {rgba(t['accent'], 120)}; }}
    #setSec {{ color: {t['accent2']}; font-size: 10px; font-weight: 800; letter-spacing: 2px; }}
    QCheckBox {{ color: {t['text']}; font-size: 13px; spacing: 8px; background: transparent; }}
    QCheckBox::indicator {{ width: 18px; height: 18px; border-radius: 5px; border: 1px solid {rgba(t['stroke'], 255)}; background: {rgba(t['input'], 220)}; }}
    QCheckBox::indicator:checked {{ background: {t['accent']}; border: 1px solid {t['accent']}; }}
#settingsDlg QComboBox {{ background: {rgba(t["input"], 220)}; border: 1px solid {rgba(t["stroke"], 200)}; border-radius: 12px; padding: 8px 12px; color: {t["text"]}; }}
#settingsDlg QComboBox QAbstractItemView {{ background: {t["card"]}; color: {t["text"]}; selection-background-color: {rgba(t["accent"], 90)}; }}
QListWidget {{ background: {rgba(t["input"], 200)}; border: 1px solid {rgba(t["stroke"], 200)}; border-radius: 14px; color: {t["text"]}; }}
QMenu {{ background: {rgba(t["card"], 240)}; border: 1px solid {rgba(t["stroke"], 160)}; border-radius: 14px; padding: 6px; }}
QMenu::item {{ padding: 7px 14px; border-radius: 9px; }}
QMenu::item:selected {{ background: {rgba(t["accent"], 60)}; }}
QScrollArea {{ border: none; }}
QScrollArea > QWidget > QWidget {{ background: transparent; }}
QScrollBar:vertical {{ background: transparent; width: 8px; margin: 3px 1px; }}
QScrollBar::handle:vertical {{ background: {rgba(t["accent"], 120)}; border-radius: 4px; min-height: 30px; }}
QScrollBar::handle:vertical:hover {{ background: {rgba(t["accent"], 200)}; }}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0px; }}
QScrollBar::add-page, QScrollBar::sub-page {{ background: transparent; }}
QScrollBar:horizontal {{ height: 0px; }}
QPushButton#toolBtn {{ background: {rgba(t['hover'], 140)}; border: none; border-radius: 10px; padding: 7px; font-size: 15px; color: {t['text']}; }}
QPushButton#toolBtn:hover {{ background: {rgba(t['hover'], 240)}; }}
QPushButton#toolBtn:pressed {{ background: {rgba(t['accent'], 70)}; }}
QLineEdit#msgInput {{ background: {rgba(t['input'], 220)}; border: 1px solid {rgba(t['stroke'], 220)}; border-radius: 18px; padding: 10px 14px; font-size: 13px; color: {t['text']}; selection-background-color: {t['accent']}; }}
QLineEdit#msgInput:focus {{ border: 1px solid {t['accent']}; background: {rgba(t['input'], 250)}; }}
QPushButton#sendBtn {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 #7c5cff, stop:1 #22d3ee); border: none; border-radius: 18px; padding: 9px 16px; color: #ffffff; font-weight: 800; font-size: 14px; }}
QPushButton#sendBtn:hover {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 #8d70ff, stop:1 #3ee0f5); }}
QPushButton#sendBtn:pressed {{ background: #6a48f0; }}
QPushButton#logoutBtn {{ background: transparent; border: none; border-radius: 8px; padding: 6px 10px; font-size: 12px; }}
QPushButton#logoutBtn:hover {{ background: rgba(255,99,99,0.16); color: #ff6767; }}
#titlebar {{ background: {rgba(t["panel"], 90)}; border-bottom: 1px solid {rgba(t["stroke"], 160)}; }}
#tbName {{ color: {t["text"]}; font-weight: 800; font-size: 13px; background: transparent; letter-spacing: 0.4px; }}
#tbBtn {{ color: {t["muted"]}; background: {rgba(t["hover"], 140)}; border: none; border-radius: 9px; font-size: 13px; }}
#tbBtn:hover {{ background: {rgba(t["hover"], 240)}; color: {t["text"]}; }}
#tbClose {{ color: {t["muted"]}; background: {rgba(t["hover"], 140)}; border: none; border-radius: 9px; font-size: 13px; }}
#tbClose:hover {{ background: #e04343; color: #ffffff; }}
#updBanner {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 {t["accent"]}, stop:1 {t["accent2"]}); border-radius: 0px; }}
#updBanner QLabel {{ color: #ffffff; font-weight: 700; background: transparent; }}
"""
def _start_embedded_server():
    """Запуск встроенного сервера в отдельном потоке"""
    try:
        import threading, importlib.util, asyncio
        p = os.path.join(DIR, "server.py")
        if not os.path.exists(p):
            print(f"   server.py не найден в {p}")
            return False
        
        print(f"   Загружаю server.py из {p}")
        spec = importlib.util.spec_from_file_location("bebsi_server", p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        
        def _run():
            try:
                print("    Встроенный сервер запускается...")
                asyncio.run(mod.main())
            except Exception as e:
                print(f"   ❌ Ошибка встроенного сервера: {e}")
                import traceback
                traceback.print_exc()
        
        t = threading.Thread(target=_run, daemon=True, name="BebsiServer")
        t.start()
        print("   ✅ Поток сервера запущен")
        return True
    except Exception as e:
        print(f"   ❌ Ошибка _start_embedded_server: {e}")
        import traceback
        traceback.print_exc()
        return False
def ensure_server():
    """=== SERVER_AUTOSTART_V3 ==="""
    def alive():
        try:
            socket.create_connection((SERVER_HOST, SERVER_PORT), timeout=1).close()
            return True
        except OSError:
            return False
    
    if alive():
        print("✅ Сервер уже работает — подключаюсь")
        return True
    
    if getattr(sys, "frozen", False):
        print("🚀 Запускаю встроенный сервер...")
        ok = _start_embedded_server()
        for _ in range(30):
            time.sleep(0.2)
            if alive():
                print("✅ Встроенный сервер поднялся")
                return True
        if ok:
            return True
        print("⚠️ Встроенный сервер не запустился")
    
    print("🔍 Ищу server.py...")
    path = os.path.join(DIR, "server.py")
    if not os.path.exists(path):
        print(f"❌ НЕ НАШЁЛ server.py в {DIR}")
        return False
    
    print("🚀 Запускаю сервер...")
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0
        
        proc = subprocess.Popen(
            [sys.executable, path],
            cwd=DIR,
            startupinfo=startupinfo,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0)
        )
        print(f"   PID сервера: {proc.pid}")
        
        for i in range(25):
            time.sleep(0.4)
            if alive():
                print(f"✅ Сервер поднялся за {i*0.4:.1f} сек")
                return True
        
        print("⚠️ Сервер не ответил за 10 секунд, но продолжаем...")
        return True
    except Exception as e:
        print(f"❌ Ошибка запуска сервера: {e}")
        return False


def grad_colors(name):
    hue = int(hashlib.md5(name.encode()).hexdigest()[:6], 16) % 360
    return QColor.fromHsl(hue, 180, 140), QColor.fromHsl((hue + 60) % 360, 200, 110)


def fmt_time(ts):
    try:
        return datetime.fromisoformat(ts).strftime("%H:%M")
    except Exception:
        return ""


def fmt_story_ts(ts):
    try:
        dt = datetime.fromisoformat(ts)
    except Exception:
        return ""
    now = datetime.now()
    hm = dt.strftime("%H:%M")
    if dt.date() == now.date():
        return f"сегодня, {hm}"
    if (now.date() - dt.date()).days == 1:
        return f"вчера, {hm}"
    return dt.strftime("%d.%m.%Y, %H:%M")


def fmt_dur(s):
    s = int(s or 0)
    return f"{s // 60}:{s % 60:02d}"


def fade_in(widget, dur=350, delay=0):
    eff = QGraphicsOpacityEffect(widget)
    widget.setGraphicsEffect(eff)
    a = QPropertyAnimation(eff, b"opacity", widget)
    a.setDuration(dur)
    a.setStartValue(0.0)
    a.setEndValue(1.0)
    a.setEasingCurve(QEasingCurve.OutCubic)
    cleanup = lambda: widget.setGraphicsEffect(None)
    if delay:
        grp = QSequentialAnimationGroup(widget)
        grp.addAnimation(QPauseAnimation(delay, widget))
        grp.addAnimation(a)
        grp.finished.connect(cleanup)
        widget._fade_anim = grp
        grp.start()
    else:
        a.finished.connect(cleanup)
        widget._fade_anim = a
        a.start()


def image_to_b64(path, max_size, quality=85):
    img = QImage(path)
    if img.isNull():
        return ""
    img = img.scaled(max_size, max_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    buf = QBuffer()
    buf.open(QIODevice.WriteOnly)
    img.save(buf, "JPG", quality)
    return bytes(buf.data().toBase64()).decode()


def wav_from_chunks(chunks, sr):
    buf = io.BytesIO()
    w = wave.open(buf, "wb")
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(sr)
    for c in chunks:
        w.writeframes(c)
    w.close()
    return buf.getvalue()


def transcribe_wav(wav_bytes):
    if not wav_bytes:
        return ""
    try:
        import vosk
    except Exception:
        return ""
    if not os.path.isdir(MODEL_PATH):
        return ""
    global VOSK_MODEL
    try:
        if VOSK_MODEL is None:
            VOSK_MODEL = vosk.Model(MODEL_PATH)
        wf = wave.open(io.BytesIO(wav_bytes))
        data = wf.readframes(wf.getnframes())
        rec = vosk.KaldiRecognizer(VOSK_MODEL, 16000)
        rec.AcceptWaveform(data)
        return json.loads(rec.FinalResult()).get("text", "")
    except Exception:
        return ""


def current_wall():
    try:
        return WALLS.get(CURRENT_PEER or "", WALL)
    except Exception:
        return WALL

def paint_wallpaper(p, w, h):
    import math as _m
    T = time.time()
    base = QColor(CUR["bg"])
    g = QLinearGradient(0, 0, 0, h)
    g.setColorAt(0, base.darker(118))
    g.setColorAt(0.55, base)
    g.setColorAt(1, base.darker(132))
    p.fillRect(0, 0, w, h, QBrush(g))
    pal = {"Классика": ("#7c5cff", "#22d3ee", "#ff5e7d"),
           "Градиент": ("#8b5cf6", "#06b6d4", "#f472b6"),
           "Горошек": ("#a78bfa", "#34d399", "#fbbf24"),
           "Звёзды": ("#818cf8", "#e879f9", "#38bdf8"),
           "Закат": ("#fb7185", "#fbbf24", "#8b5cf6"),
           "Океан": ("#0ea5e9", "#22d3ee", "#6366f1"),
           "Сакура": ("#f472b6", "#fb7185", "#a78bfa")}.get(current_wall(), ("#7c5cff", "#22d3ee", "#ff5e7d"))
    p.setPen(Qt.NoPen)
    for i, col in enumerate(pal):
        c = QColor(col); c.setAlpha(34)
        cx = w * (0.5 + 0.36 * _m.sin(T * 0.11 + i * 2.1))
        cy = h * (0.5 + 0.34 * _m.cos(T * 0.09 + i * 1.7))
        r = max(w, h) * (0.34 + 0.06 * _m.sin(T * 0.23 + i))
        rg = QRadialGradient(cx, cy, r)
        rg.setColorAt(0, c)
        c2 = QColor(col); c2.setAlpha(0)
        rg.setColorAt(1, c2)
        p.setBrush(QBrush(rg))
        p.drawEllipse(QPointF(cx, cy), r, r)
    for i in range(46):
        sx = (i * 137.5) % w
        sy = (h + 60 - ((T * (6 + (i % 5) * 3) + i * 61) % (h + 120)))
        a = 40 + int(30 * _m.sin(T * 1.3 + i))
        c = QColor("#ffffff"); c.setAlpha(max(10, a))
        p.setBrush(c); p.setPen(Qt.NoPen)
        p.drawEllipse(QPointF(sx, sy), 1.6 + (i % 3), 1.6 + (i % 3))
    for k in range(3):
        col = QColor(pal[k]); col.setAlpha(26)
        pen = QPen(col); pen.setWidth(26); pen.setCapStyle(Qt.RoundCap)
        p.setPen(pen); p.setBrush(Qt.NoBrush)
        path = QPainterPath()
        y0 = h * (0.30 + 0.22 * k)
        path.moveTo(-40, y0)
        x = -40
        while x < w + 40:
            y = y0 + 26 * _m.sin(x / 150.0 + T * (0.5 + 0.17 * k) + k * 2.0)
            path.lineTo(x, y)
            x += 24
        p.drawPath(path)
    p.setPen(Qt.NoPen)
    vg = QRadialGradient(w / 2, h / 2, max(w, h) * 0.75)
    vc = QColor("#000000"); vc.setAlpha(0)
    vg.setColorAt(0.6, vc)
    vc2 = QColor("#000000"); vc2.setAlpha(120)
    vg.setColorAt(1, vc2)
    p.setBrush(QBrush(vg))
    p.drawRect(0, 0, w, h)
def is_big_emoji(text):
    t = (text or "").strip()
    if not t or len(t) > 8:
        return False
    chars = [ch for ch in t if ch not in "\ufe0f\u200d "]
    if not chars:
        return False
    return all(ord(ch) > 0x1F000 or 0x2600 <= ord(ch) <= 0x27BF
               or 0x2B00 <= ord(ch) <= 0x2BFF for ch in chars)


def make_pop_wav():
    path = os.path.join(tempfile.gettempdir(), "bebsi_pop.wav")
    if os.path.exists(path):
        return path
    sr = 22050
    nn = int(sr * 0.18)
    buf = io.BytesIO()
    w = wave.open(buf, "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    for i in range(nn):
        t = i / sr
        env = (1 - i / nn) ** 2
        v = int(12000 * env * math.sin(2 * math.pi * (600 + 300 * (1 - i / nn)) * t))
        w.writeframes(v.to_bytes(2, "little", signed=True))
    w.close()
    with open(path, "wb") as f:
        f.write(buf.getvalue())
    return path


class OptionBar(QFrame):
    clicked = Signal()

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.frac = 0.0
        self.count = 0
        self.total = 0
        self.setFixedHeight(38)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName("optbar")
        self.setStyleSheet(f"#optbar {{background:{rgba(CUR['bubble'], 200)}; "
                           f"border:1px solid {rgba(CUR['stroke'], 255)}; border-radius:12px;}}")
        self.fill = QWidget(self)
        self.fill.setStyleSheet(f"background:{rgba(CUR['accent'], 120)}; border-radius:12px;")
        self.fill.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.fill.lower()
        h = QHBoxLayout(self)
        h.setContentsMargins(12, 0, 10, 0)
        self.lb = QLabel(text)
        self.lb.setStyleSheet(f"background:transparent; border:none; color:{CUR['text']}; font-size:13px; font-weight:600;")
        self.lb.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.pc = QLabel(APP_NAME)
        self.pc.setStyleSheet(f"background:transparent; border:none; color:{CUR['muted']}; font-size:11px;")
        self.pc.setAttribute(Qt.WA_TransparentForMouseEvents)
        h.addWidget(self.lb, 1)
        h.addWidget(self.pc)

    def set_state(self, frac, count, total):
        self.frac = frac
        self.count = count
        self.total = total
        self.pc.setText(f"{int(frac * 100)}% ({count})" if total else "")
        self._resize_fill()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._resize_fill()

    def _resize_fill(self):
        w = int(self.width() * max(0.0, min(1.0, self.frac)))
        self.fill.setGeometry(1, 1, max(0, w - 2), self.height() - 2)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mouseReleaseEvent(e)


class PollOpt(QPushButton):
    def __init__(self, text, parent=None, mine=False):
        super().__init__(parent)
        self.opt_text = text
        self.mine = mine
        self.cnt = 0
        self.total = 0
        self.setFixedHeight(36)
        self.setCursor(Qt.PointingHandCursor)

    def update_stat(self, cnt, total):
        self.cnt = cnt
        self.total = total
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        r = self.rect()
        p.setPen(Qt.NoPen)
        _base = QColor("#ffffff") if self.mine else QColor(CUR["stroke"])
        _base.setAlpha(32 if self.mine else 110)
        p.setBrush(_base)
        p.drawRoundedRect(r, 8, 8)
        if self.total:
            w = int(r.width() * self.cnt / self.total)
            if w > 0:
                col = QColor(CUR["accent"]); col.setAlpha(130)
                p.setBrush(col)
                p.drawRoundedRect(0, 0, w, r.height(), 8, 8)
        p.setPen(QColor("#ffffff"))
        f = p.font(); f.setBold(True); f.setPixelSize(13); p.setFont(f)
        p.drawText(r.adjusted(12, 0, -40, 0), Qt.AlignVCenter | Qt.AlignLeft, self.opt_text)
        if self.total:
            p.drawText(r.adjusted(0, 0, -12, 0), Qt.AlignVCenter | Qt.AlignRight, str(self.cnt))


class PollW(QWidget):
    vote = Signal(int)

    def __init__(self, poll_str, parent=None, mine=False):
        super().__init__(parent)
        self.mine = mine
        self.vv = QVBoxLayout(self)
        self.vv.setContentsMargins(0, 2, 0, 2)
        self.vv.setSpacing(6)
        try:
            self.p = json.loads(poll_str) if isinstance(poll_str, str) else poll_str
        except Exception:
            self.p = {}
        if not isinstance(self.p, dict):
            self.p = {}
        self.opts = self.p.get("opts", self.p.get("options", self.p.get("answers", [])))
        self.qtext = self.p.get("q", self.p.get("question", self.p.get("title", "")))
        self.votes = self.p.get("votes", {}) or {}
        if self.qtext:
            q = QLabel(self.qtext)
            q.setWordWrap(True)
            q.setStyleSheet("font-weight:700; font-size:14px;")
            self.vv.addWidget(q)
        self.rows = []
        for i, opt in enumerate(self.opts):
            b = PollOpt(str(opt), mine=self.mine)
            b.clicked.connect(lambda _, i=i: (print("голос ->", i), self.vote.emit(i)))
            self.vv.addWidget(b)
            self.rows.append(b)
        self.total_lbl = QLabel(APP_NAME)
        self.total_lbl.setStyleSheet(f"font-size:11px; color:{_meta_color(self.mine)};")
        self.vv.addWidget(self.total_lbl)
        self.refresh()

    def set_poll_votes(self, votes):
        self.votes = votes or {}
        self.refresh()

    def refresh(self):
        total = sum(len(v) for v in self.votes.values())
        for i, b in enumerate(self.rows):
            b.update_stat(len(self.votes.get(str(i), [])), total)
        self.total_lbl.setText(f"Всего голосов: {total}" if total else "Нет голосов")


class WaveStatic(QWidget):
 def __init__(self, b64, parent=None):
  super().__init__(parent)
  self.setFixedSize(60, 26)
  self.peaks = self._peaks(b64)
 def _peaks(self, b64, n=12):
  try:
   import base64, wave as _w, io as _io, array
   data = base64.b64decode(b64)
   if len(data) > 4 and data[:4] != b"RIFF":
    raw = data
   else:
    wf = _w.open(_io.BytesIO(data))
    raw = wf.readframes(wf.getnframes())
   a = array.array("h")
   a.frombytes(raw[:len(raw) // 2 * 2])
   if not a:
    return [4] * n
   step = max(1, len(a) // n)
   out = []
   for i in range(n):
    ch = a[i * step:(i + 1) * step] or [0]
    out.append(max(abs(min(ch)), abs(max(ch)), 1))
   mx = max(out) or 1
   return [max(2, int(v * 22 / mx)) for v in out]
  except Exception:
   return [4] * 12
 def paintEvent(self, e):
  p = QPainter(self)
  p.setRenderHint(QPainter.Antialiasing)
  p.setPen(Qt.NoPen)
  p.setBrush(QColor(CUR["accent"]))
  for i, h in enumerate(self.peaks):
   p.drawRoundedRect(i * 5, (26 - h) // 2, 3, h, 1, 1)
  p.end()

LINK_RE = re.compile(r"https?://[^\s<>\"']+")
_LINK_CACHE = {}
class LinkFetch(QThread):
    done = Signal(str, dict)
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
        try:
            import urllib.request, html as _h
            from urllib.parse import urlparse
            req = urllib.request.Request(self.url, headers={"User-Agent": "Mozilla/5.0 (BebsiBot)"})
            with urllib.request.urlopen(req, timeout=6) as r:
                raw = r.read(400000)
                ctype = r.headers.get("Content-Type", "")
            if "text/html" not in ctype:
                self.done.emit(self.url, {})
                return
            page = raw.decode("utf-8", "ignore")
            def og(n):
                m = (re.search(r'<meta[^>]+property=["\']og:' + n + r'["\'][^>]+content=["\']([^"\']+)["\']', page, re.I)
                     or re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:' + n + r'["\']', page, re.I))
                return _h.unescape(m.group(1)).strip() if m else ""
            title = og("title")
            if not title:
                m = re.search(r"<title[^>]*>([^<]+)</title>", page, re.I)
                title = _h.unescape(m.group(1)).strip() if m else ""
            desc = og("description")
            site = urlparse(self.url).netloc.lower()
            if site.startswith("www."):
                site = site[4:]
            img = ""
            iu = og("image")
            if iu.startswith("http"):
                try:
                    with urllib.request.urlopen(iu, timeout=6) as r2:
                        data = r2.read(300000)
                    if data[:3] in (b"\xff\xd8\xff", b"\x89PG"):
                        img = base64.b64encode(data).decode()
                except Exception:
                    img = ""
            self.done.emit(self.url, {"url": self.url, "title": title[:120], "desc": desc[:220], "site": site, "image": img})
        except Exception:
            self.done.emit(self.url, {})

class MessageBubble(QWidget):
    react = Signal(int, str)
    picker = Signal(int)
    view = Signal(str)
    view_video = Signal(str, str)
    file_save = Signal(str, str)
    ctx = Signal(dict)
    poll_vote_sig = Signal(int, int)

    def __init__(self, text, ts, mine, media="", sender_name="",
                 voice="", vdur=0.0, video="", transcript="", reply_name="",
                 reply_text="", fwd="", file_name="", file_data="", edited=False,
                 poll="", animate=True, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName("bubbleMine" if mine else "bubbleOther")
        self.setMaximumWidth(540)
        self.setStyleSheet("QWidget#bubbleMine{min-height:0; padding:4px 6px;}"
                           "QWidget#bubbleOther{min-height:0; padding:4px 6px;}")
        self.mine = mine
        self.mid = None
        self._time = fmt_time(ts)
        self._read = False
        self._edited = bool(edited)
        self._txt_text = text
        self._base = text
        self._disp = sender_name or ("Вы" if mine else "")
        self.media_b64 = media
        self.video_b64 = video
        self.transcript = transcript
        self.voice_b64 = voice
        self.vdur = vdur
        self.file_name = file_name
        self.file_data = file_data
        self.player = None
        self.ao = None
        v = QVBoxLayout(self)
        v.setContentsMargins(12, 6, 12, 4)
        v.setSpacing(3)
        if fwd:
            fl = QLabel("⇄ " + fwd)
            fl.setStyleSheet(f"font-size:11px; font-weight:700; color:{CUR['accent']};")
            v.addWidget(fl)
        if reply_text:
            qf = QFrame()
            qf.setStyleSheet(f"background:{CUR['bubble'] if mine else CUR['bg']}; border-left:3px solid {CUR['accent']}; border-radius:6px;")
            qv = QVBoxLayout(qf)
            qv.setContentsMargins(8, 4, 8, 4)
            qv.setSpacing(1)
            qn = QLabel(reply_name or "")
            qn.setStyleSheet(f"font-weight:700; color:{CUR['accent']}; border:none;")
            qt = QLabel(reply_text[:80])
            qt.setWordWrap(True)
            qt.setStyleSheet("border:none;")
            qv.addWidget(qn)
            qv.addWidget(qt)
            v.addWidget(qf)
        if sender_name and not mine:
            sn = QLabel(sender_name)
            sn.setStyleSheet(f"font-weight:700; color:{CUR['accent']}; font-size:12px;")
            v.addWidget(sn)
        if media:
            try:
                import base64
                from PySide6.QtGui import QImage


                img = QImage()
                img.loadFromData(base64.b64decode(_(media)))
                lb = QLabel()
                from PySide6.QtGui import QPixmap
                pm = QPixmap.fromImage(img.scaledToWidth(min(260, max(120, img.width()))))
                lb.setPixmap(pm)
                lb.setCursor(Qt.PointingHandCursor)
                lb.mouseReleaseEvent = lambda e: self.view.emit(self.media_b64)
                v.addWidget(lb)
            except Exception as ex:
                print("MEDIA DRAW ERR:", ex)
        if video:
            vb = QPushButton("▶  Кружок" + (f"  ({int(vdur)} с)" if vdur else ""))
            vb.setCursor(Qt.PointingHandCursor)
            vb.clicked.connect(lambda: self.view_video.emit(self.video_b64, self.transcript))
            v.addWidget(vb)
            if transcript:
                tl = QLabel("🗣 " + transcript)
                tl.setWordWrap(True)
                tl.setStyleSheet("font-size:12px;")
                v.addWidget(tl)
        if voice:
            hr = QHBoxLayout()
            hr.setSpacing(6)
            self.play_btn = IconBtn("play", 30)
            self.play_btn.clicked.connect(self._play_voice)
            self.tr_btn = IconBtn("transcript", 30)
            self.tr_btn.setToolTip("Расшифровка")
            self.tr_btn.clicked.connect(self._transcribe)
            dl = QLabel(f"{int(vdur // 60)}:{int(vdur % 60):02d}")
            dl.setStyleSheet("font-size:11px;")
            hr.addWidget(self.play_btn)
            self.rate_btn = QPushButton("1x")
            self.rate_btn.setFixedWidth(30)
            self.rate_btn.setStyleSheet("border:none;font-size:10px;font-weight:800;")
            self.rate_btn.clicked.connect(self._cycle_rate)
            hr.addWidget(self.rate_btn)
            try:
                hr.addWidget(WaveStatic(self.voice_b64))
            except Exception:
                pass
            hr.addWidget(dl)
            hr.addStretch(1)
            hr.addWidget(self.tr_btn)
            vw = QWidget(); vw.setLayout(hr)
            v.addWidget(vw)
            self.tr_lbl = QLabel(APP_NAME)
            self.tr_lbl.setWordWrap(True)
            self.tr_lbl.setStyleSheet("font-size:12px;")
            self.tr_lbl.hide()
            v.addWidget(self.tr_lbl)
        if file_data or file_name:
            fb = QPushButton("📄 " + (file_name or "Файл"))
            fb.setCursor(Qt.PointingHandCursor)
            fb.clicked.connect(lambda _c=False: self.file_save.emit(self.file_name, self.file_data))
            v.addWidget(fb)
        if poll:
            try:
                self.poll_data = json.loads(poll) if isinstance(poll, str) else poll
            except Exception:
                self.poll_data = {"question": "", "options": [], "votes": {}}
            self.poll_w = PollW(self.poll_data, mine=mine)
            v.addWidget(self.poll_w)
        else:
            self.poll_w = None
        if text:
            self.txt = QLabel()
            self.txt.setWordWrap(True)
            self.txt.setStyleSheet(f"font-size:{FONT_SZ}px;")
            self.txt.setTextFormat(Qt.RichText)
            self.txt.setTextInteractionFlags(Qt.TextSelectableByMouse)
            self.txt.setContextMenuPolicy(Qt.NoContextMenu)
            self._base = text
            v.addWidget(self.txt)
            self._render_text()
        self.link_w = None
        _u = LINK_RE.search(self._base or "")
        if _u:
            self._link_url = _u.group(0)
            if self._link_url in _LINK_CACHE:
                self._build_link(_LINK_CACHE[self._link_url])
            else:
                self._fetch = LinkFetch(self._link_url)
                self._fetch.done.connect(self._on_link)
                self._fetch.start()
        bot = QHBoxLayout()
        self._bot = bot
        bot.setSpacing(4)
        bot.addStretch(1)
        self._edited = edited
        if self._edited:
            el = QLabel("изменено")
            el.setStyleSheet(f"font-size:10px; color:{_meta_color(mine)};")
            bot.addWidget(el)
        self.chk = QLabel(APP_NAME)
        self.chk.setStyleSheet(f"font-size:10px; color:{_meta_color(mine)};")
        bot.addWidget(self.chk)
        self.tl2 = QLabel(self._time + (" · изменено" if self._edited else ""))
        self.tl2.setStyleSheet(f"font-size:10px; color:{_meta_color(mine)};")
        bot.addWidget(self.tl2)
        bw = QWidget(); bw.setLayout(bot)
        self._bw = bw
        bw.setFixedHeight(16)
        v.addWidget(bw)
        bw.hide()
        self.react_row = QHBoxLayout()
        self.react_row.setSpacing(4)
        self.react_row.addStretch(1)
        self.react_w = QWidget(); self.react_w.setLayout(self.react_row)
        self.react_w.hide()
        v.addWidget(self.react_w)
        if mine:
            self.chk.setText("✓")
        self._update_checks()

    def _on_link(self, url, d):
        try:
            _LINK_CACHE[url] = d
            if getattr(self, "_link_url", None) == url and not self.link_w:
                self._build_link(d)
        except Exception:
            pass
    def _build_link(self, d):
        try:
            if not d or not (d.get("title") or d.get("desc") or d.get("image")):
                return
            w = QFrame()
            w.setStyleSheet(f"background:{rgba(CUR['bubble'], 220)}; border:1px solid {rgba(CUR['stroke'], 200)}; border-radius:12px;")
            vl = QVBoxLayout(w)
            vl.setContentsMargins(10, 8, 10, 8)
            vl.setSpacing(4)
            if d.get("image"):
                try:
                    img = QImage()
                    img.loadFromData(base64.b64decode(_(d["image"])))
                    lb = QLabel()
                    lb.setPixmap(QPixmap.fromImage(img.scaledToWidth(240, Qt.SmoothTransformation)))
                    lb.setStyleSheet("border-radius:8px;")
                    vl.addWidget(lb)
                except Exception:
                    pass
            st = QLabel(d.get("site") or "")
            st.setStyleSheet(f"color:{CUR['accent2']}; font-size:11px; font-weight:700; background:transparent; border:none;")
            vl.addWidget(st)
            if d.get("title"):
                tt = QLabel(d["title"])
                tt.setWordWrap(True)
                tt.setStyleSheet("font-weight:700; font-size:13px; background:transparent; border:none;")
                vl.addWidget(tt)
            if d.get("desc"):
                ds = QLabel(d["desc"])
                ds.setWordWrap(True)
                ds.setStyleSheet(f"color:{CUR['muted']}; font-size:12px; background:transparent; border:none;")
                vl.addWidget(ds)
            w.setCursor(Qt.PointingHandCursor)
            w.mouseReleaseEvent = lambda e: QDesktopServices.openUrl(QUrl(d["url"]))
            self.link_w = w
            lay = self.layout()
            idx = lay.indexOf(self._bw) if getattr(self, "_bw", None) is not None else -1
            if idx < 0:
                idx = lay.count()
            lay.insertWidget(idx, w)

        except Exception:
            pass
    def _render_text(self):
        import html as _h
        col = "rgba(255,255,255,0.75)" if self.mine else rgba(CUR['muted'], 235)
        marks = " ✓✓" if (self.mine and self._read) else (" ✓" if self.mine else "")
        body = _h.escape(getattr(self, "_base", "") or getattr(self, "_txt_text", ""))
        body = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", body)
        body = re.sub(r"\*(.+?)\*", r"<b>\1</b>", body)
        body = re.sub(r"__([^_]+)__", r"<i>\1</i>", body)
        body = re.sub(r"_([^_]+)_", r"<i>\1</i>", body)
        body = re.sub(r"`([^`]+)`", r"<code>\1</code>", body)
        meta = f'<span style="font-size:10px; color:{col};">{self._time + (" · изменено" if self._edited else "")}{marks}</span>'
        self.txt.setText(f"{body}<br>{meta}" if body else meta)

    def set_read(self):
        self._read = True
        self._render_text()

    def set_text(self, t):
        self._txt_text = t
        self._base = t
        self._edited = True
        if getattr(self, "tl2", None): self.tl2.setText(self._time + " · изменено")
        if getattr(self, "txt", None) is not None:
            self._render_text()

    def _update_checks(self):
        if self.mine:
            self.chk.setText("✓✓" if self._read else "✓")

    def _transcribe(self):
        try:
            import base64
            txt = transcribe_wav(base64.b64decode(self.voice_b64))
        except Exception:
            txt = ""
        self.tr_lbl.setText(txt or "Не удалось расшифровать 🤷")
        self.tr_lbl.show()

    def _play_voice(self):
        try:
            import base64, tempfile
            from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


            from PySide6.QtCore import QUrl


            data = base64.b64decode(self.voice_b64)
            if len(data) > 4 and data[:4] != b"RIFF":
                import wave, io
                buf = io.BytesIO()
                w = wave.open(buf, "wb")
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000)
                w.writeframes(data); w.close()
                data = buf.getvalue()
            tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            tmp.write(data); tmp.close()
            if self.player is None:
                self.player = QMediaPlayer(self)
                self.ao = QAudioOutput(self)
                self.player.setAudioOutput(self.ao)
                self.player.mediaStatusChanged.connect(self._on_voice_end)
            self.player.setSource(QUrl.fromLocalFile(tmp.name))
            self.player.play()
            self.player.setPlaybackRate(getattr(self, "_rate", 1.0))
            self.play_btn.kind = "stop"; self.play_btn.update()
        except Exception:
            pass

    def _cycle_rate(self):
     r = getattr(self, "_rate", 1.0)
     r = 1.5 if r == 1.0 else (2.0 if r == 1.5 else 1.0)
     self._rate = r
     self.rate_btn.setText(f"{r:g}x")
     if self.player is not None:
      self.player.setPlaybackRate(r)
    
    def _on_voice_end(self, st):
        from PySide6.QtMultimedia import QMediaPlayer


        if st == QMediaPlayer.EndOfMedia:
            self.play_btn.kind = "play"; self.play_btn.update()

    def set_reactions(self, reactions, me):
        if getattr(self, "react_w", None) is not None and reactions:
            self.react_w.show()
        while self.react_row.count():
            it = self.react_row.takeAt(0)
            w = it.widget()
            if w:
                w.deleteLater()
        for emo, users in (reactions or {}).items():
            b = QPushButton(f"{emo} {len(users)}")
            b.setFixedHeight(22)
            b.setCursor(Qt.PointingHandCursor)
            if me in users:
                b.setStyleSheet(f"border:1px solid {CUR['accent']}; border-radius:11px; color:{CUR['text']}; font-size:12px; padding:0 8px; background:rgba(255,255,255,0.10);")
            else:
                b.setStyleSheet(f"border:1px solid rgba(128,128,128,60); border-radius:11px; color:{CUR['text']}; font-size:12px; padding:0 8px; background:rgba(255,255,255,0.05);")
            b.clicked.connect(lambda _, e=emo: self.react.emit(getattr(self, "mid", 0) or 0, e))
            self.react_row.insertWidget(0, b)
        self.react_row.addStretch(1)

    def set_poll_votes(self, votes):
        if self.poll_w is not None:
            self.poll_w.set_poll_votes(votes)

    def mouseDoubleClickEvent(self, e):
        self.picker.emit(getattr(self, "mid", 0) or 0)
        super().mouseDoubleClickEvent(e)

    def contextMenuEvent(self, e):
        self.ctx.emit({"text": self._txt_text, "name": self._disp,
                       "mine": self.mine, "mid": self.mid,
                       "sel": (self.txt.selectedText() if getattr(self, "txt", None) is not None else "")})

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.RightButton:
            self.contextMenuEvent(e)
        super().mouseReleaseEvent(e)


class VoiceRecorder(QObject):
    finished_rec = Signal(bytes, float)

    def __init__(self):
        super().__init__()
        self._stream = None
        self._frames = []
        self._t0 = 0

    def start(self):
        import sounddevice as sd
        self._frames = []
        self._t0 = time.time()
        self._stream = sd.InputStream(samplerate=16000, channels=1, dtype="int16",
                                      callback=lambda i, f, t, s: self._frames.append(i.copy()))
        self._stream.start()

    def stop(self):
        dur = max(0.0, time.time() - self._t0) if self._t0 else 0
        try:
            if self._stream is not None:
                self._stream.stop()
                self._stream.close()
        except Exception:
            pass
        self._stream = None
        try:
            import numpy as np
            import wave, io
            data = np.concatenate(self._frames) if self._frames else np.zeros((1600, 1), dtype="int16")
            buf = io.BytesIO()
            w = wave.open(buf, "wb")
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000)
            w.writeframes(data.tobytes()); w.close()
            wav = buf.getvalue()
        except Exception:
            wav = b""
        self._t0 = 0
        self.finished_rec.emit(wav, dur)


class CircleRecorder(QObject):
    finished_rec = Signal(bytes, bytes, float)

    def __init__(self):
        super().__init__()
        self._cap = None
        self._writer = None
        self._tmp = None
        self._audio = []
        self._astream = None
        self._left = 8
        self._t0 = 0
        self._ft = QTimer(self)
        self._ft.setInterval(33)
        self._ft.timeout.connect(self._grab)
        self._ct = QTimer(self)
        self._ct.setInterval(1000)
        self._ct.timeout.connect(self._sec)

    def start(self):
        import cv2
        import sounddevice as sd
        import tempfile
        test = cv2.VideoCapture(CAM_DEV if CAM_DEV >= 0 else 0)
        ok_cam = test.isOpened()
        test.release()
        if not ok_cam:
            self._t0 = 0
            self.finished_rec.emit(b"", b"", 0.0)
            return
        self._tmp = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False).name
        self._cap = cv2.VideoCapture(CAM_DEV if CAM_DEV >= 0 else 0)
        self._writer = cv2.VideoWriter(self._tmp, cv2.VideoWriter_fourcc(*"mp4v"), 15, (480, 480))
        self._audio = []
        self._astream = sd.InputStream(samplerate=16000, channels=1, dtype="int16",
                                       callback=lambda i, f, t, s: self._audio.append(i.copy()))
        self._astream.start()
        self._t0 = time.time()
        self._left = 8
        self._ft.start()
        self._ct.start()

    def _grab(self):
        try:
            if self._cap is not None and self._writer is not None:
                ok, frame = self._cap.read()
                if ok:
                    import cv2
                    self._writer.write(cv2.resize(frame, (480, 480)))
        except Exception:
            pass

    def _sec(self):
        self._left -= 1
        if self._left <= 0:
            self.stop()

    def stop(self):
        self._ft.stop()
        self._ct.stop()
        dur = max(0.0, time.time() - self._t0) if self._t0 else 0
        try:
            if self._astream is not None:
                self._astream.stop()
                self._astream.close()
        except Exception:
            pass
        try:
            import numpy as np
            import wave, io
            data = np.concatenate(self._audio) if self._audio else np.zeros((1600, 1), dtype="int16")
            buf = io.BytesIO()
            w = wave.open(buf, "wb")
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000)
            w.writeframes(data.tobytes()); w.close()
            wav = buf.getvalue()
        except Exception:
            wav = b""
        try:
            if self._writer is not None:
                self._writer.release()
            if self._cap is not None:
                self._cap.release()
            mp4 = open(self._tmp, "rb").read() if self._tmp else b""
        except Exception:
            mp4 = b""
        self._t0 = 0
        self.finished_rec.emit(mp4, wav, dur)


class ImageViewer(QDialog):
    def __init__(self, parent, b64):
        super().__init__(parent)
        self.setWindowTitle("Фото")
        self.setStyleSheet(f"background:{CUR['bg']};")
        v = QVBoxLayout(self)
        try:
            import base64
            from PySide6.QtGui import QImage


            img = QImage()
            img.loadFromData(base64.b64decode(_(b64)))
            lb = QLabel()
            lb.setPixmap(QPixmap.fromImage(img.scaledToWidth(min(600, max(200, img.width())))))
            v.addWidget(lb)
        except Exception:
            v.addWidget(QLabel("не удалось открыть фото"))


class VideoDialog(QDialog):
    def __init__(self, parent, b64, transcript=""):
        super().__init__(parent)
        self.setWindowTitle("Кружок")
        self.resize(420, 560)
        self.setStyleSheet(f"background:{CUR['bg']};")
        v = QVBoxLayout(self)
        try:
            import base64, tempfile
            from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


            from PySide6.QtMultimediaWidgets import QVideoWidget


            from PySide6.QtCore import QUrl


            tmp = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
            tmp.write(base64.b64decode(_(b64))); tmp.close()
            self.mp = QMediaPlayer(self)
            self.ao = QAudioOutput(self)
            self.mp.setAudioOutput(self.ao)
            vw = QVideoWidget(self)
            self.mp.setVideoOutput(vw)
            v.addWidget(vw)
            if transcript:
                tl = QLabel("🗣 " + transcript)
                tl.setWordWrap(True)
                v.addWidget(tl)
            self.mp.setSource(QUrl.fromLocalFile(tmp.name))
            self.mp.play()
        except Exception:
            v.addWidget(QLabel("не удалось открыть видео"))


class ScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setStyleSheet("QScrollArea{background:transparent; border:none;}")


def _(s):
    if not s:
        return s
    if s.startswith("data:") and "," in s:
        s = s.split(",", 1)[1]
    s = s.strip().replace("\n", "").replace(" ", "")
    s += "=" * (-len(s) % 4)
    return s


import os as _os
EXTRA_PATH = os.path.join(DIR, "extra.json")
try:
    _ex = json.load(open(EXTRA_PATH, encoding="utf-8"))
except Exception:
    _ex = {}
BLOCKED = set(_ex.get("blocked", []))
CONTACTS = set(_ex.get("contacts", []))
DELETED = set(_ex.get("deleted", []))
CONTACT_NAMES = _ex.get("names", {})
PINNED = set(_ex.get("pinned", []))
DRAFTS = _ex.get("drafts", {})
SCHED = _ex.get("sched", {})
WALLS = _ex.get("walls", {})
FONT_SZ = int(_ex.get("font_sz", 14))
CURRENT_PEER = ""
MUTES = set(_ex.get("mutes", []))
PINS_MSG = _ex.get("pins_msg", {})
_dnd = _ex.get("dnd", [False, 23, 7])
DND_ON = bool(_dnd[0])
DND_FROM = int(_dnd[1])
DND_TO = int(_dnd[2])
SOUND_ON = bool(_ex.get("sound", True))
TOASTS_ON = bool(_ex.get("toasts", True))

import time as _time_mod
APP_START = _time_mod.time()

MANUAL_AUTH = False

def save_extra():
    try:
        json.dump({"blocked": list(BLOCKED), "contacts": list(CONTACTS),
                   "deleted": list(DELETED), "names": CONTACT_NAMES, "pinned": list(PINNED), "drafts": DRAFTS, "mutes": list(MUTES), "pins_msg": PINS_MSG, "dnd": [DND_ON, DND_FROM, DND_TO], "sound": SOUND_ON, "toasts": TOASTS_ON, "walls": WALLS, "font_sz": FONT_SZ},
                  open(EXTRA_PATH, "w", encoding="utf-8"))
    except Exception:
        pass


class SplashLogo(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet("background:transparent;")
        self.t = 0.0

    def start(self):
        try:
            from PySide6.QtCore import QVariantAnimation
            w = self.window()
            self.setParent(w)
            self.setGeometry(0, 0, w.width(), w.height())
            self.show()
            self.raise_()
            self.a = QVariantAnimation(self)
            self.a.setDuration(1900)
            self.a.setStartValue(0.0)
            self.a.setEndValue(1.0)
            self.a.valueChanged.connect(self._tick)
            self.a.finished.connect(self.deleteLater)
            self.a.start()
        except Exception as ex:
            print("SPLASH ERR:", ex)

    def _tick(self, v):
        self.t = v
        self.update()

    def paintEvent(self, e):
        try:
            from PySide6.QtCore import QPointF, QRectF
            from PySide6.QtGui import QLinearGradient
            p = QPainter(self)
            p.setRenderHint(QPainter.Antialiasing)
            p.fillRect(self.rect(), QColor(CUR["bg"]))
            t = self.t
            W, H = self.width(), self.height()
            cx0, cy0 = W / 2, H / 2 - 20
            cx1, cy1 = 33, 69
            r0, r1 = 62, 17
            if t < 0.3:
                k = t / 0.3
                k = k * k * (3 - 2 * k)
                cx, cy, r = cx0, cy0, r0 * (0.5 + 0.5 * k)
                alpha = k
            elif t < 0.85:
                k = (t - 0.3) / 0.55
                k = k * k * (3 - 2 * k)
                cx = cx0 + (cx1 - cx0) * k
                cy = cy0 + (cy1 - cy0) * k
                r = r0 + (r1 - r0) * k
                alpha = 1.0
            else:
                k = (t - 0.85) / 0.15
                cx, cy, r = cx1, cy1, r1
                alpha = 1.0 - k
            p.setOpacity(max(0.0, min(1.0, alpha)))
            g = QLinearGradient(cx - r, cy - r, cx + r, cy + r)
            g.setColorAt(0, QColor("#2ecc71"))
            g.setColorAt(1, QColor("#3498db"))
            p.setBrush(g)
            p.setPen(Qt.NoPen)
            p.drawEllipse(QPointF(cx, cy), r, r)
            p.setPen(QColor("#ffffff"))
            f = p.font(); f.setBold(True); f.setPixelSize(max(10, int(r * 0.95)))
            p.setFont(f)
            p.drawText(QRectF(cx - r, cy - r, 2 * r, 2 * r), Qt.AlignCenter, APP_NAME[:1].upper())
            if t < 0.55:
                p.setOpacity(max(0.0, alpha * (1 - t / 0.55)))
                f2 = p.font(); f2.setPixelSize(30); f2.setBold(True)
                p.setFont(f2)
                p.setPen(QColor(CUR["text"]))
                p.drawText(QRectF(0, cy0 + r0 + 24, W, 44), Qt.AlignCenter, APP_NAME)
        except Exception as ex:
            print("SPLASH PAINT ERR:", ex)



class AvatarWidget(QWidget):
    clicked = Signal(str)

    def __init__(self, name, size=40, show_dot=False, clickable=False, ring=False, parent=None):
        super().__init__(parent)
        self.name = name
        self.sz = size
        self.show_dot = show_dot
        self.clickable = clickable
        self.ring = ring
        self.online = False
        self.avatar_b64 = ""
        self.setFixedSize(size, size)
        if clickable:
            self.setCursor(Qt.PointingHandCursor)
        self._pulse = False
        self._pt = QTimer(self)
        self._pt.setInterval(2000)
        self._pt.timeout.connect(self._tick_pulse)

    def set_online(self, on):
        self.online = on
        if on:
            pass
        else:
            self._pt.stop()
        self.update()

    def _tick_pulse(self):
        self._pulse = not self._pulse
        if self.show_dot and self.online and self.isVisible() and "Избранное" not in str(self.name):
            self.update()

    def set_name(self, t):
        self.name = t
        self.update()

    def set_avatar_b64(self, b64):
        self.avatar_b64 = b64 or ""
        self.update()

    def mouseReleaseEvent(self, e):
        if self.clickable and e.button() == Qt.LeftButton:
            self.clicked.emit(self.name)
        super().mouseReleaseEvent(e)

    def paintEvent(self, e):
        from PySide6.QtGui import QLinearGradient, QBrush, QImage


        import base64
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        if self.ring:
            p.setPen(QPen(QColor(CUR["accent"]), 2.5))
            p.setBrush(Qt.NoBrush)
            p.drawEllipse(self.rect().adjusted(1, 1, -1, -1))
        m = 4 if self.ring else 0
        r = self.rect().adjusted(m, m, -m, -m)
        cols = ["#e74c3c", "#f39c12", "#2ecc71", "#3498db", "#9b59b6", "#e91e63", "#1abc9c"]
        h = sum(ord(ch) for ch in (self.name or "?"))
        # _AV_LETTER_FIX
        drawn = False
        if self.avatar_b64:
            try:
                img = QImage()
                img.loadFromData(base64.b64decode(self.avatar_b64))
                p.setBrush(QBrush(img.scaled(self.sz, self.sz, Qt.KeepAspectRatioByExpanding)))
                p.setPen(Qt.NoPen)
                p.drawEllipse(r)
                drawn = True
            except Exception:
                self.avatar_b64 = ""
        if not drawn:
            g = QLinearGradient(0, 0, self.sz, self.sz)
            g.setColorAt(0, QColor(cols[h % len(cols)]))
            g.setColorAt(1, QColor(cols[(h // 7) % len(cols)]))
            p.setBrush(g)
            p.setPen(Qt.NoPen)
            p.drawEllipse(r)
            p.setPen(QColor("#ffffff"))
            f = p.font(); f.setBold(True); f.setPixelSize(int(self.sz * 0.4))
            p.setFont(f)
            p.drawText(r, Qt.AlignCenter, (self.name or "?")[:1].upper())
        if self.show_dot and "Избранное" not in str(self.name):
            d = max(8, self.sz // 4) + (2 if getattr(self, "_pulse", False) else 0)
            p.setPen(QPen(QColor(CUR["bg"]), 2))
            p.setBrush(QColor("#2ecc71") if self.online else QColor(CUR["muted"]))
            p.drawEllipse(self.sz - d - 1, self.sz - d - 1, d, d)


class TypingDots(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.i = 0
        self.setFixedSize(28, 12)
        self.t = QTimer(self)
        self.t.setInterval(300)
        self.t.timeout.connect(self.step)

    def step(self):
        self.i = (self.i + 1) % 4
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setPen(Qt.NoPen)
        for k in range(3):
            on = (self.i + k) % 4 != 3
            p.setBrush(QColor(CUR["text"]) if on else QColor(CUR["muted"]))
            p.drawEllipse(2 + k * 10, 3, 6, 6)

    def start(self): self.t.start()
    def stop(self): self.t.stop()


class CrossBtn(QPushButton):
    def __init__(self, size=22, parent=None):
        super().__init__(parent)
        self.setFixedSize(size, size)
        self.setCursor(Qt.PointingHandCursor)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        pen = QPen(QColor(CUR["text"]), 2, Qt.SolidLine, Qt.RoundCap)
        p.setPen(pen)
        c = self.rect().center()
        d = self.width() // 4
        p.drawLine(c.x() - d, c.y() - d, c.x() + d, c.y() + d)
        p.drawLine(c.x() - d, c.y() + d, c.x() + d, c.y() - d)


class IconBtn(QPushButton):
    def __init__(self, kind, size=40, parent=None):
        super().__init__(parent)
        self.kind = kind
        self._bg = None
        self.active = False
        self.setFixedSize(size, size)
        self.setCursor(Qt.PointingHandCursor)

    def setStyleSheet(self, s):
        s = s or ""
        i = s.find("background:")
        col = None
        if i != -1:
            j = s.find(";", i)
            col = s[i + 11:j if j != -1 else len(s)].strip()
        self._bg = col if col and col.startswith("#") else None
        self.update()

    def enterEvent(self, e):
        self.update(); super().enterEvent(e)

    def leaveEvent(self, e):
        self.update(); super().leaveEvent(e)

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        r = self.rect()
        if self._bg:
            p.setBrush(QColor(self._bg)); p.setPen(Qt.NoPen)
            p.drawRoundedRect(r, 12, 12)
        col = QColor("#e74c3c" if self.active else
                     (CUR["text"] if self.underMouse() else CUR["muted"]))
        pen = QPen(col); pen.setWidth(2); pen.setCapStyle(Qt.RoundCap); p.setPen(pen)
        c = r.center()
        if self.kind == "mic":
            p.setBrush(col); p.setPen(Qt.NoPen)
            p.drawRoundedRect(c.x() - 5, c.y() - 12, 10, 15, 5, 5)
            p.setPen(pen)
            p.drawArc(c.x() - 9, c.y() - 6, 18, 15, 200 * 16, 140 * 16)
            p.drawLine(c.x(), c.y() + 9, c.x(), c.y() + 12)
            p.drawLine(c.x() - 6, c.y() + 12, c.x() + 6, c.y() + 12)
        elif self.kind == "circle":
            p.setPen(QPen(col, 2, Qt.SolidLine, Qt.RoundCap))
            p.setBrush(Qt.NoBrush)
            p.drawRoundedRect(c.x() - 4, c.y() - 9.5, 8, 4, 1.5, 1.5)
            p.drawRoundedRect(c.x() - 10, c.y() - 6.5, 20, 14, 4, 4)
            p.drawEllipse(c.x() - 3.5, c.y() - 3, 7, 7)
            p.setBrush(col); p.setPen(Qt.NoPen)
            p.drawEllipse(c.x() - 1.2, c.y() - 0.7, 2.4, 2.4)
        elif self.kind == "send":
            p.setBrush(col); p.setPen(Qt.NoPen)
            p.drawPolygon([QPoint(c.x() - 9, c.y() - 10), QPoint(c.x() + 11, c.y()),
                           QPoint(c.x() - 9, c.y() + 10), QPoint(c.x() - 5, c.y())])
        elif self.kind == "attach":
            p.translate(c.x(), c.y()); p.rotate(45)
            p.drawRoundedRect(-6, -11, 12, 17, 6, 6)
            p.drawLine(0, -7, 0, 2)
        elif self.kind == "emoji":
            p.drawEllipse(c.x() - 8, c.y() - 8, 16, 16)
            p.setBrush(col); p.setPen(Qt.NoPen)
            p.drawEllipse(c.x() - 4, c.y() - 4, 2, 2)
            p.drawEllipse(c.x() + 2, c.y() - 4, 2, 2)
            p.setPen(pen)
            p.drawArc(c.x() - 5, c.y() - 2, 10, 9, 200 * 16, 140 * 16)
        elif self.kind == "play":
            p.setBrush(col); p.setPen(Qt.NoPen)
            p.drawPolygon([QPoint(c.x() - 4, c.y() - 6), QPoint(c.x() - 4, c.y() + 6), QPoint(c.x() + 6, c.y())])
        elif self.kind == "stop":
            p.setBrush(col); p.setPen(Qt.NoPen)
            p.drawRoundedRect(c.x() - 5, c.y() - 5, 10, 10, 2, 2)
        elif self.kind == "transcript":
            p.setPen(QPen(col, 2, Qt.SolidLine, Qt.RoundCap))
            p.drawLine(c.x() - 6, c.y() - 5, c.x() + 6, c.y() - 5)
            p.drawLine(c.x() - 6, c.y(), c.x() + 6, c.y())
            p.drawLine(c.x() - 6, c.y() + 5, c.x() + 2, c.y() + 5)
        elif self.kind == "call":
            p.setPen(Qt.NoPen); p.setBrush(col)
            p.translate(c.x(), c.y()); p.rotate(-45)
            p.drawRoundedRect(-7, -2, 14, 4, 2, 2)
            p.drawEllipse(-9, -4, 6, 8)
            p.drawEllipse(3, -4, 6, 8)
        elif self.kind == "vcam":
            p.setPen(QPen(col, 2)); p.setBrush(Qt.NoBrush)
            p.drawRoundedRect(c.x() - 9, c.y() - 5, 11, 10, 2, 2)
            p.setBrush(col); p.setPen(Qt.NoPen)
            p.drawPolygon([QPoint(c.x() + 3, c.y() - 3), QPoint(c.x() + 9, c.y() - 6), QPoint(c.x() + 9, c.y() + 6), QPoint(c.x() + 3, c.y() + 3)])
        elif self.kind == "min":
            p.setPen(QPen(col, 2, Qt.SolidLine, Qt.RoundCap))
            p.drawLine(c.x() - 6, c.y(), c.x() + 6, c.y())
        elif self.kind == "max":
            p.setPen(QPen(col, 2))
            p.setBrush(Qt.NoBrush)
            p.drawRoundedRect(c.x() - 5, c.y() - 5, 11, 11, 2, 2)
        elif self.kind == "close":
            p.setPen(QPen(col, 2, Qt.SolidLine, Qt.RoundCap))
            p.drawLine(c.x() - 5, c.y() - 5, c.x() + 5, c.y() + 5)
            p.drawLine(c.x() - 5, c.y() + 5, c.x() + 5, c.y() - 5)
        elif self.kind == "lock":
            p.setPen(QPen(col, 2, Qt.SolidLine, Qt.RoundCap))
            p.setBrush(Qt.NoBrush)
            p.drawRoundedRect(c.x() - 6, c.y() - 1, 12, 10, 2, 2)
            p.drawArc(c.x() - 4, c.y() - 8, 8, 8, 0, 180 * 16)
        elif self.kind == "people":
            p.setPen(QPen(col, 2, Qt.SolidLine, Qt.RoundCap))
            p.setBrush(Qt.NoBrush)
            p.drawEllipse(c.x() - 8, c.y() - 8, 7.5, 7.5)
            p.drawArc(c.x() - 11, c.y() + 0, 13, 10, 0, 180 * 16)
            p.drawEllipse(c.x() + 2, c.y() - 7, 6, 6)
            p.drawArc(c.x() + 0.5, c.y() + 1, 10, 8, 0, 180 * 16)


class ChatItem(QFrame):
    clicked = Signal(str)
    ctx = Signal(str, object)

    def __init__(self, name, is_group=False, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.name = name
        self.selected = False
        self.setObjectName("chatItem")
        self.setCursor(Qt.PointingHandCursor)
        h = QHBoxLayout(self)
        h.setContentsMargins(10, 8, 12, 8)
        h.setSpacing(10)
        self.avatar = AvatarWidget(name, 40, show_dot=(not is_group and name != "saved"))
        mid = QVBoxLayout()
        mid.setSpacing(2)
        self.nm = QLabel(name)
        self.nm.setObjectName("itemName")
        self.last = QLabel("Нет сообщений")
        self.last.setObjectName("itemLast")
        self.last.setMaximumWidth(150)
        self.nm.setMaximumWidth(150)
        mid.addWidget(self.nm)
        mid.addWidget(self.last)
        meta = QVBoxLayout()
        meta.setSpacing(4)
        self.tlbl = QLabel(APP_NAME)
        self.tlbl.setObjectName("itemTime")
        self.tlbl.setMinimumWidth(34)
        self.tlbl.setMaximumWidth(44)
        self.badge = QLabel("0")
        self.badge.setObjectName("badge")
        self.badge.setAlignment(Qt.AlignCenter)
        self.badge.hide()
        meta.addWidget(self.tlbl, 0, Qt.AlignRight)
        meta.addWidget(self.badge, 0, Qt.AlignRight)
        meta.addStretch(1)
        h.addWidget(self.avatar)
        h.addLayout(mid, 1)
        h.addLayout(meta)

    def set_display(self, t): self.nm.setText(t)
    def set_online(self, on): self.avatar.set_online(on)

    def set_last(self, text, ts="", prefix="", ticks=""):
        try:
            text = text or ""
            self.last_txt = (text[:60] + "...") if len(text) > 60 else text
            self.last_ts = ts
            lbl = getattr(self, "last", None) or getattr(self, "lbl2", None)
            if lbl is not None:
                lbl.setText((prefix or "") + self.last_txt)
            tl = getattr(self, "tlbl", None)
            if tl is not None:
                s = str(ts or "")
                t = s[11:16] if len(s) >= 16 else s
                tl.setText(((ticks + " ") if ticks else "") + t)
        except Exception:
            pass
    def set_unread(self, n):
        if n > 0:
            was = self.badge.isHidden()
            self.badge.setText(str(n))
            self.badge.show()
            if was:
                fade_in(self.badge, 200)
                self.badge.setStyleSheet("font-size:15px;")
                QTimer.singleShot(130, lambda: self.badge.setStyleSheet("font-size:10px;"))
        else:
            self.badge.hide()

    def set_selected(self, sel):
        if sel == self.selected:
            return
        self.selected = sel
        self.setProperty("selected", sel)
        self.style().unpolish(self)
        self.style().polish(self)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.clicked.emit(self.name)
        super().mouseReleaseEvent(e)

    def contextMenuEvent(self, e):
        self.ctx.emit(self.name, e.globalPos())
        super().contextMenuEvent(e)

class PreviewDialog(QDialog):
    def __init__(self, parent, b64):
        super().__init__(parent)
        self.setWindowTitle("Предпросмотр")
        fade_in(self, 250)
        self.setStyleSheet(f"background:{CUR['bg']};")
        v = QVBoxLayout(self)
        try:
            import base64
            from PySide6.QtGui import QImage, QPixmap


            img = QImage()
            img.loadFromData(base64.b64decode(_(b64)))
            lb = QLabel()
            lb.setPixmap(QPixmap.fromImage(img.scaledToWidth(min(420, max(160, img.width())))))
            v.addWidget(lb)
        except Exception:
            v.addWidget(QLabel("не удалось открыть фото"))
        self.cap = QLineEdit()
        self.cap.setPlaceholderText("Подпись...")
        v.addWidget(self.cap)
        row = QHBoxLayout()
        okb = QPushButton("Отправить")
        okb.setObjectName("primaryBtn")
        okb.clicked.connect(self.accept)
        cb = QPushButton("Отмена")
        cb.setObjectName("ghostBtn")
        cb.clicked.connect(self.reject)
        row.addStretch(1)
        row.addWidget(okb)
        row.addWidget(cb)
        bw = QWidget(); bw.setLayout(row)
        v.addWidget(bw)
    def caption(self):
        return self.cap.text()
        fade_in(self, 250)

class PollDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Новый опрос")
        fade_in(self, 250)
        self.setStyleSheet(f"background:{CUR['bg']};")
        v = QVBoxLayout(self)
        self.q = QLineEdit()
        self.q.setPlaceholderText("Вопрос")
        v.addWidget(self.q)
        self.opts_l = QVBoxLayout()
        self.opt_rows = []
        v.addLayout(self.opts_l)
        add_b = QPushButton("+ Добавить вариант")
        add_b.setObjectName("ghostBtn")
        add_b.clicked.connect(self.add_opt)
        v.addWidget(add_b)
        self.add_opt()
        self.add_opt()
        row = QHBoxLayout()
        okb = QPushButton("Создать")
        okb.setObjectName("primaryBtn")
        okb.clicked.connect(self.accept)
        cb = QPushButton("Отмена")
        cb.setObjectName("ghostBtn")
        cb.clicked.connect(self.reject)
        row.addStretch(1)
        row.addWidget(okb)
        row.addWidget(cb)
        bw = QWidget(); bw.setLayout(row)
        v.addWidget(bw)

    def add_opt(self):
        le = QLineEdit()
        le.setPlaceholderText("Вариант")
        self.opts_l.addWidget(le)
        self.opt_rows.append(le)

    def _build(self):
        opts = [le.text().strip() for le in self.opt_rows if le.text().strip()]
        return {"q": self.q.text().strip(), "opts": opts, "votes": {}}

    def poll_json(self):
        return json.dumps(self._build(), ensure_ascii=False)

    def poll(self):
        return self.poll_json()

    def data(self):
        return self.poll_json()

    def result_data(self):
        return (self.q.text().strip(),
                [le.text().strip() for le in self.opt_rows if le.text().strip()])
        fade_in(self, 250)

class Confetti(QWidget):
    def __init__(self, anchor):
        super().__init__(anchor)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setGeometry(0, 0, anchor.width(), anchor.height())
        self.ps = []
        for i in range(70):
            self.ps.append([random.uniform(0, self.width()), -30 - random.uniform(0, 250),
                            random.uniform(3, 7),
                            random.choice(["#ff5e7d", "#ffd166", "#6c5ce7", "#00cec9", "#2ecc71"]),
                            random.uniform(4, 9)])
        self.t = QTimer(self)
        self.t.setInterval(30)
        self.t.timeout.connect(self.step)
        self.t.start()
        QTimer.singleShot(2000, self.deleteLater)
        self.show()
        self.raise_()
        self.raise_()

    def step(self):
        for p in self.ps:
            p[1] += p[2]
            p[0] += math.sin(p[1] / 18)
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        try:
            for pt in self.ps:
                p.setBrush(QColor(pt[3]))
                p.setPen(Qt.NoPen)
                p.drawRoundedRect(pt[0], pt[1], pt[4], pt[4] * 0.7, 2, 2)
        except Exception:
            pass


class WaveformWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.i = 0
        self.setFixedSize(54, 34)
        self.t = QTimer(self)
        self.t.setInterval(180)
        self.t.timeout.connect(self.step)

    def _paint(self, i):
        self.update()

    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        hs = [10, 22, 14]
        for k in range(3):
            h = hs[(k + self.i) % 3]
            p.setBrush(QColor(CUR["accent"]))
            p.setPen(Qt.NoPen)
            p.drawRoundedRect(8 + k * 16, (34 - h) / 2, 6, h, 3, 3)

    def step(self):
        self.i = (self.i + 1) % 3
        self._paint(self.i)

    def start(self): self.t.start()
    def stop(self): self.t.stop()


class EmojiDialog(QDialog):
    def __init__(self, parent, on_pick):
        super().__init__(parent)
        self.setWindowTitle("Смайлики")
        g = QGridLayout(self)
        g.setSpacing(2)
        g.setContentsMargins(10, 10, 10, 10)
        emojis = [e for e in EMOJIS if len(e.strip()) > 1 or (e.strip() and e.strip() != "\ufe0f" and ord(e.strip()[0]) > 0x2000)]
        for i, e in enumerate(emojis):
            b = QPushButton(e)
            b.setObjectName("emojiBtn")
            b.setFixedSize(44, 44)
            b.clicked.connect(lambda _, e=e: on_pick(e))
            g.addWidget(b, i // 10, i % 10)


class GroupDialog(QDialog):
    def __init__(self, parent, users):
        super().__init__(parent)
        self.setWindowTitle("Новая группа")
        self.setFixedWidth(320)
        v = QVBoxLayout(self)
        v.setSpacing(12)
        self.name_ed = QLineEdit()
        self.name_ed.setPlaceholderText("Название группы")
        v.addWidget(self.name_ed)
        self.list = QListWidget()
        for u in users:
            it = QListWidgetItem(u[1])
            it.setData(Qt.UserRole, u[0])
            it.setFlags(it.flags() | Qt.ItemIsUserCheckable)
            it.setCheckState(Qt.Unchecked)
            self.list.addItem(it)
        v.addWidget(self.list)
        btn = QPushButton("Создать")
        btn.clicked.connect(self.accept)
        v.addWidget(btn)

    def result_data(self):
        members = []
        for i in range(self.list.count()):
            it = self.list.item(i)
            if it.checkState() == Qt.Checked:
                members.append(it.data(Qt.UserRole))
        return self.name_ed.text().strip(), members


class GroupInfoDialog(QDialog):
    def __init__(self, parent, display, members, owner, chats):
        super().__init__(parent)
        self.setWindowTitle("Группа")
        self.setFixedWidth(340)
        v = QVBoxLayout(self)
        v.setContentsMargins(24, 24, 24, 24)
        self.setStyleSheet(f"#settingsDlg {{ background: {CUR['card']}; }}")
        cst = f"QComboBox {{ background: {CUR['input']}; border: 1px solid {CUR['stroke']}; border-radius: 12px; padding: 8px 12px; color: {CUR['text']}; font-size: 13px; }}"
        v.setSpacing(10)
        t = QLabel(display)
        t.setObjectName("peerName")
        t.setAlignment(Qt.AlignCenter)
        v.addWidget(t)
        s = QLabel(f"Участников: {len(members)}")
        s.setObjectName("subtitle")
        s.setAlignment(Qt.AlignCenter)
        v.addWidget(s)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        w = QWidget()
        lay = QVBoxLayout(w)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(6)
        for m in members:
            row = QHBoxLayout()
            row.setSpacing(10)
            av = AvatarWidget(m, 34)
            av.set_avatar_b64(chats.get(m, {}).get("avatar", ""))
            nm = QLabel(chats.get(m, {}).get("display", m))
            nm.setObjectName("itemName")
            sub = QLabel("· владелец" if m == owner else "@" + m)
            sub.setObjectName("subtitle")
            row.addWidget(av)
            row.addWidget(nm)
            row.addWidget(sub, 1)
            lay.addLayout(row)
        lay.addStretch(1)
        scroll.setWidget(w)
        v.addWidget(scroll)
        btn = QPushButton("Закрыть")
        btn.clicked.connect(self.reject)
        v.addWidget(btn)


PEER_DLG_QSS = f"""
QDialog#peerDlg {{ background: {rgba(CUR['card'], 240)}; border-radius:22px; border:1px solid {rgba(CUR['stroke'], 160)}; }}
QLabel#statusPill {{ background: {rgba(CUR['bubble'], 220)}; border:1px solid {rgba(CUR['stroke'], 200)}; border-radius:12px; padding:5px 14px; font-size:12px; color:{CUR['muted']}; }}
QLabel#statusPill[online="true"] {{ color:{CUR['online']}; border:1px solid {rgba(CUR['online'], 120)}; background:{rgba(CUR['online'], 26)}; }}
QFrame#segBar {{ background: {rgba(CUR['bubble'], 200)}; border:1px solid {rgba(CUR['stroke'], 180)}; border-radius:16px; }}
QPushButton#segBtn {{ background:transparent; border:none; border-radius:12px; padding:8px 6px; font-size:12px; font-weight:700; color:{CUR['muted']}; }}
QPushButton#segBtn:hover {{ background: {rgba(CUR['hover'], 200)}; color:{CUR['text']}; }}
QPushButton#segBtn[sel="true"] {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 {CUR['accent']}, stop:1 {CUR['accent2']}); color:#ffffff; }}
QScrollArea#pageScroll {{ background:transparent; border:none; }}
QFrame#mediaRow {{ background: {rgba(CUR['bubble'], 200)}; border:1px solid {rgba(CUR['stroke'], 180)}; border-radius:14px; }}
QFrame#mediaRow:hover {{ background: {rgba(CUR['hover'], 220)}; border:1px solid {rgba(CUR['accent'], 140)}; }}
QLabel#mediaRowTitle {{ font-size:13px; font-weight:700; color:{CUR['text']}; background:transparent; }}
QLabel#mediaRowSub {{ font-size:11px; color:{CUR['muted']}; background:transparent; }}
"""
class _RoundThumb(QWidget):
    clicked = Signal()
    def __init__(self, b64, size=96, parent=None):
        super().__init__(parent)
        self.setFixedSize(size, size)
        self.setCursor(Qt.PointingHandCursor)
        self._pm = QPixmap()
        try:
            import base64
            img = QImage()
            if img.loadFromData(base64.b64decode(_(b64))):
                self._pm = QPixmap.fromImage(img.scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        except Exception:
            pass
        self._hover = False
    def enterEvent(self, e):
        self._hover = True; self.update(); super().enterEvent(e)
    def leaveEvent(self, e):
        self._hover = False; self.update(); super().leaveEvent(e)
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mouseReleaseEvent(e)
    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        r = self.rect()
        path = QPainterPath()
        path.addRoundedRect(float(r.x()), float(r.y()), float(r.width()), float(r.height()), 14, 14)
        p.setClipPath(path)
        if not self._pm.isNull():
            p.drawPixmap(r, self._pm)
        else:
            p.fillRect(r, QColor(CUR["bubble"]))
        if self._hover:
            c = QColor("#ffffff"); c.setAlpha(38)
            p.fillRect(r, c)
        p.setClipping(False)
        pen = QPen(QColor(CUR["accent2"] if self._hover else CUR["stroke"]))
        pen.setWidth(2 if self._hover else 1)
        p.setPen(pen)
        p.setBrush(Qt.NoBrush)
        p.drawRoundedRect(r.adjusted(1, 1, -1, -1), 14, 14)
        p.end()
class _MediaRow(QFrame):
    clicked = Signal()
    def __init__(self, icon, title, sub="", parent=None):
        super().__init__(parent)
        self.setCursor(Qt.PointingHandCursor)
        self.setObjectName("mediaRow")
        h = QHBoxLayout(self)
        h.setContentsMargins(12, 10, 12, 10)
        h.setSpacing(10)
        ic = QLabel(icon)
        ic.setStyleSheet("font-size:18px; background:transparent;")
        col = QVBoxLayout()
        col.setSpacing(2)
        t = QLabel(title)
        t.setObjectName("mediaRowTitle")
        col.addWidget(t)
        if sub:
            s = QLabel(sub)
            s.setObjectName("mediaRowSub")
            col.addWidget(s)
        h.addWidget(ic)
        h.addLayout(col, 1)
        ar = QLabel("›")
        ar.setStyleSheet("color:%s; font-size:16px; background:transparent;" % CUR["muted"])
        h.addWidget(ar)
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mouseReleaseEvent(e)
class PeerInfoDialog(QDialog):
    def __init__(self, chat, key):
        super().__init__(chat)
        self.chat = chat
        self.key = key
        c = chat.chats.get(key, {})
        is_grp = str(key).startswith("g")
        is_saved = key == "saved"
        is_chan = str(key).startswith("c") and str(key)[1:].isdigit()
        self.setWindowTitle("Профиль")
        self.setFixedWidth(430)
        self.setObjectName("peerDlg")
        self.setStyleSheet(PEER_DLG_QSS)
        v = QVBoxLayout(self)
        v.setContentsMargins(26, 24, 26, 22)
        v.setSpacing(12)
        close_row = QHBoxLayout()
        close_row.addStretch(1)
        cx = QPushButton("✕")
        cx.setObjectName("closeBtn")
        cx.setFixedSize(32, 32)
        cx.clicked.connect(self.accept)
        close_row.addWidget(cx)
        v.addLayout(close_row)
        av = AvatarWidget((chat.my_profile["display"] or chat.me) if is_saved else (c.get("display") or key), 88, ring=True)
        av.set_avatar_b64(chat.my_profile.get("avatar", "") if is_saved else c.get("avatar", ""))
        v.addWidget(av, 0, Qt.AlignHCenter)
        nm = QLabel(("🔖 Избранное" if is_saved else (CONTACT_NAMES.get(key) or c.get("display") or key)))
        nm.setObjectName("peerName")
        nm.setAlignment(Qt.AlignCenter)
        v.addWidget(nm)
        on = c.get("online", False)
        if is_saved:
            sub_text = "твои личные заметки"
        elif is_chan:
            sub_text = f"Подписчиков: {len(c.get('members', []))}"
        elif is_grp:
            sub_text = f"Участников: {len(c.get('members', []))}"
        else:
            sub_text = "в сети" if on else ("был(а) в сети в " + (chat.last_seen.get(key) or "—"))
        pill = QLabel(sub_text)
        pill.setObjectName("statusPill")
        pill.setAlignment(Qt.AlignCenter)
        if not is_grp and not is_saved and not is_chan and on:
            pill.setProperty("online", "true")
            pill.style().unpolish(pill)
            pill.style().polish(pill)
        v.addWidget(pill, 0, Qt.AlignHCenter)
        if not is_grp and not is_saved and c.get("bio"):
            b = QLabel(c["bio"])
            b.setWordWrap(True)
            b.setObjectName("subtitle")
            b.setAlignment(Qt.AlignCenter)
            v.addWidget(b)
        msgs = chat.cache.get(key, []) or []
        self.photos = [m for m in msgs if m.get("media")]
        self.circles = [m for m in msgs if m.get("video")]
        self.voices = [m for m in msgs if m.get("voice")]
        self.files = [m for m in msgs if (m.get("file_data") or m.get("file_name")) and not m.get("media")]
        seg = QFrame()
        seg.setObjectName("segBar")
        sh = QHBoxLayout(seg)
        sh.setContentsMargins(6, 6, 6, 6)
        sh.setSpacing(6)
        self._seg_btns = []
        tabs = [("📷", "Фото", len(self.photos)), ("⭕", "Кружки", len(self.circles)),
                ("🎤", "Голосовые", len(self.voices)), ("📄", "Файлы", len(self.files))]
        for i, (ic, lb, cn) in enumerate(tabs):
            b = QPushButton(f"{ic} {lb} · {cn}")
            b.setObjectName("segBtn")
            b.setCursor(Qt.PointingHandCursor)
            b.clicked.connect(lambda _, i=i: self._show_page(i))
            sh.addWidget(b)
            self._seg_btns.append(b)
        v.addWidget(seg)
        self.stack = QStackedWidget()
        self.stack.addWidget(self._photos_page())
        self.stack.addWidget(self._list_page(self.circles, True, False))
        self.stack.addWidget(self._list_page(self.voices, False, True))
        self.stack.addWidget(self._list_page(self.files, False, False))
        v.addWidget(self.stack, 1)
        self._show_page(0)
    def _show_page(self, i):
        self.stack.setCurrentIndex(i)
        for j, b in enumerate(self._seg_btns):
            b.setProperty("sel", "true" if j == i else "false")
            b.style().unpolish(b)
            b.style().polish(b)
    def _photos_page(self):
        sw = QScrollArea()
        sw.setWidgetResizable(True)
        sw.setObjectName("pageScroll")
        w = QWidget()
        g = QGridLayout(w)
        g.setContentsMargins(10, 10, 10, 10)
        g.setSpacing(8)
        if not self.photos:
            g.addWidget(self._empty("📷", "Пока нет фото"), 0, 0)
        for i, m in enumerate(self.photos):
            th = _RoundThumb(m["media"], 96)
            th.clicked.connect(lambda mm=m: ImageViewer(self.chat, mm["media"]).exec())
            g.addWidget(th, i // 3, i % 3)
        sw.setWidget(w)
        return sw
    def _list_page(self, items, is_video, is_voice):
        sw = QScrollArea()
        sw.setWidgetResizable(True)
        sw.setObjectName("pageScroll")
        w = QWidget()
        vl = QVBoxLayout(w)
        vl.setContentsMargins(10, 10, 10, 10)
        vl.setSpacing(8)
        if not items:
            vl.addWidget(self._empty("⭕" if is_video else ("🎤" if is_voice else "📄"),
                                      "Пока нет " + ("кружков" if is_video else ("голосовых" if is_voice else "файлов"))))
        for m in items:
            if is_video:
                row = _MediaRow("⭕", f"Кружок · {int(m.get('vdur') or 0)} с", (m.get("transcript") or "")[:60])
                row.clicked.connect(lambda mm=m: VideoDialog(self.chat, mm["video"], mm.get("transcript", "")).exec())
            elif is_voice:
                row = _MediaRow("🎤", f"Голосовое · {int(m.get('vdur') or 0)} с", (m.get("transcript") or "")[:60])
                row.clicked.connect(lambda mm=m: self._play_voice(mm["voice"]))
            else:
                row = _MediaRow("📄", m.get("file_name") or "Файл", "нажми, чтобы сохранить")
                row.clicked.connect(lambda mm=m: self.chat.open_file(mm.get("file_name", "Файл"), mm.get("file_data", "")))
            vl.addWidget(row)
        vl.addStretch(1)
        sw.setWidget(w)
        return sw
    def _empty(self, icon, text):
        w = QWidget()
        vl = QVBoxLayout(w)
        vl.setSpacing(6)
        vl.setContentsMargins(0, 24, 0, 24)
        a = QLabel(icon)
        a.setAlignment(Qt.AlignCenter)
        a.setStyleSheet("font-size:34px; background:transparent;")
        t = QLabel(text)
        t.setAlignment(Qt.AlignCenter)
        t.setObjectName("subtitle")
        vl.addWidget(a)
        vl.addWidget(t)
        return w
    def _play_voice(self, b64):
        try:
            import base64, tempfile
            from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
            from PySide6.QtCore import QUrl
            data = base64.b64decode(b64)
            if len(data) > 4 and data[:4] != b"RIFF":
                import wave, io
                buf = io.BytesIO()
                w = wave.open(buf, "wb")
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(16000)
                w.writeframes(data); w.close()
                data = buf.getvalue()
            tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
            tmp.write(data); tmp.close()
            if getattr(self, "_mp", None) is None:
                self._mp = QMediaPlayer(self)
                self._ao = QAudioOutput(self)
                self._mp.setAudioOutput(self._ao)
            self._mp.setSource(QUrl.fromLocalFile(tmp.name))
            self._mp.play()
        except Exception:
            pass

class ChannelSettingsDialog(QDialog):
    def __init__(self, chat, key):
        super().__init__(chat)
        self.chat = chat
        self.key = key
        c = chat.chats.get(key, {})
        self.setWindowTitle("Настройки канала")
        self.setFixedWidth(420)
        v = QVBoxLayout(self)
        v.setContentsMargins(24, 24, 24, 24)
        v.setSpacing(10)
        t = QLabel(c.get("display") or key)
        t.setObjectName("peerName")
        t.setAlignment(Qt.AlignCenter)
        v.addWidget(t)
        self.name_ed = QLineEdit((c.get("display") or "").replace("📢 ", ""))
        self.name_ed.setPlaceholderText("Название канала")
        v.addWidget(self.name_ed)
        self.desc_ed = QLineEdit(c.get("desc") or "")
        self.desc_ed.setPlaceholderText("Описание")
        v.addWidget(self.desc_ed)
        sub = QLabel("Подписчики:")
        sub.setObjectName("subtitle")
        v.addWidget(sub)
        self.sub_l = QVBoxLayout()
        self.sub_l.setSpacing(6)
        v.addLayout(self.sub_l)
        self._fill_subs()
        row = QHBoxLayout()
        save = QPushButton("Сохранить")
        save.setObjectName("sendBtn")
        save.clicked.connect(self.save)
        row.addWidget(save)
        dele = QPushButton("🗑 Удалить канал")
        dele.setObjectName("ghostBtn")
        dele.clicked.connect(self.delete_chan)
        row.addWidget(dele)
        bw = QWidget(); bw.setLayout(row)
        v.addWidget(bw)
    def _fill_subs(self):
        while self.sub_l.count():
            it = self.sub_l.takeAt(0)
            w = it.widget()
            if w:
                w.deleteLater()
        c = self.chat.chats.get(self.key, {})
        for u in (c.get("members") or []):
            r = QHBoxLayout()
            lb = QLabel(("👑 " if u == c.get("owner") else "") + u)
            lb.setObjectName("subtitle")
            r.addWidget(lb, 1)
            if u != c.get("owner"):
                kb = QPushButton("Кик")
                kb.setObjectName("ghostBtn")
                kb.setFixedWidth(60)
                kb.clicked.connect(lambda _, uu=u: self.kick(uu))
                r.addWidget(kb)
            wr = QWidget(); wr.setLayout(r)
            self.sub_l.addWidget(wr)
    def kick(self, u):
        self.chat.send_pkt({"type": "channel_kick", "id": int(str(self.key)[1:]), "user": u})
        QTimer.singleShot(600, self._refresh)
    def _refresh(self):
        self.chat.send_pkt({"type": "channels"})
    def save(self):
        cid = int(str(self.key)[1:])
        nm = self.name_ed.text().strip()
        if nm:
            self.chat.send_pkt({"type": "channel_rename", "id": cid, "name": nm[:40]})
        self.chat.send_pkt({"type": "channel_set", "id": cid, "desc": self.desc_ed.text().strip()[:120]})
        self.chat.show_warn("Настройки сохранены ⚙")
        QTimer.singleShot(600, self._refresh)
    def delete_chan(self):
        ok = QInputDialog.getText(self, "Удалить канал", "Точно удалить канал и все посты? Напиши: УДАЛИТЬ")
        if ok and ok[0].strip() == "УДАЛИТЬ":
            self.chat.send_pkt({"type": "channel_delete", "id": int(str(self.key)[1:])})
            self.chat.close_chat()
            self.accept()

class StoryViewer(QDialog):
    def __init__(self, parent, flat, idx):
        super().__init__(parent)
        self.flat = flat
        self.idx = idx
        self.setFixedSize(420, 640)
        v = QVBoxLayout(self)
        v.setSpacing(8)
        top = QHBoxLayout()
        self.who = QLabel()
        self.who.setObjectName("peerName")
        close = QPushButton("×")
        close.setObjectName("closeBtn")
        close.setFixedSize(36, 36)
        close.clicked.connect(self.reject)
        top.addWidget(self.who, 1)
        top.addWidget(close)
        v.addLayout(top)
        self.img = QLabel()
        self.img.setAlignment(Qt.AlignCenter)
        self.img.setStyleSheet(f"background:{rgba(CUR['bubble'], 210)}; border-radius:20px;")
        v.addWidget(self.img, 1)
        self.cap = QLabel()
        self.cap.setWordWrap(True)
        self.cap.setAlignment(Qt.AlignCenter)
        self.cap.setObjectName("subtitle")
        v.addWidget(self.cap)
        self.counter = QLabel()
        self.counter.setObjectName("subtitle")
        self.counter.setAlignment(Qt.AlignCenter)
        v.addWidget(self.counter)
        self.t = QTimer(self)
        self.t.setInterval(5000)
        self.t.timeout.connect(self.next)
        self.show_idx(idx)
        self.t.start()
        fade_in(self.img, 300)

    def show_idx(self, i):
        if not self.flat:
            return
        self.idx = i % len(self.flat)
        user, disp, s = self.flat[self.idx]
        self.who.setText(f"{disp}  ·  {fmt_story_ts(s['ts'])}")
        pix = QPixmap()
        if pix.loadFromData(QByteArray.fromBase64(QByteArray(s["media"].encode()))):
            self.img.setPixmap(pix.scaled(380, 500, Qt.KeepAspectRatio,
                             Qt.SmoothTransformation))
        self.cap.setText(s.get("caption") or "")
        self.counter.setText(f"{self.idx + 1} / {len(self.flat)}")

    def next(self): self.show_idx(self.idx + 1)
    def prev(self): self.show_idx(self.idx - 1)

    def mouseReleaseEvent(self, e):
        if e.position().x() < self.width() / 3:
            self.prev()
        else:
            self.next()
        super().mouseReleaseEvent(e)


class ProfileDialog(QDialog):
    def __init__(self, parent=None, own=False, username="", display="", bio="", avatar=""):
        super().__init__(parent)
        self.own = own
        self.avatar_b64 = avatar
        self.setWindowTitle("Профиль")
        self.setFixedWidth(340)
        v = QVBoxLayout(self)
        v.setContentsMargins(24, 24, 24, 24)
        v.setSpacing(12)
        self.av = AvatarWidget(username, 96, clickable=own)
        if own:
            self.av.clicked.connect(self.pick_avatar)
        self.av.set_avatar_b64(avatar)
        v.addWidget(self.av, 0, Qt.AlignHCenter)
        un = QLabel("@" + username)
        un.setObjectName("subtitle")
        un.setAlignment(Qt.AlignCenter)
        v.addWidget(un)
        if own:
            self.name_ed = QLineEdit(display)
            self.name_ed.setPlaceholderText("Отображаемое имя")
            self.bio_ed = QLineEdit(bio)
            self.bio_ed.setPlaceholderText("Пара слов о себе")
            v.addWidget(self.name_ed)
            v.addWidget(self.bio_ed)
            hint = QLabel("Кликни по фото, чтобы сменить его")
            hint.setObjectName("subtitle")
            hint.setAlignment(Qt.AlignCenter)
            v.addWidget(hint)
            btn = QPushButton("Сохранить")
            btn.clicked.connect(self.accept)
            v.addWidget(btn)
        else:
            d = QLabel(display or username)
            d.setObjectName("peerName")
            d.setAlignment(Qt.AlignCenter)
            v.addWidget(d)
            b = QLabel(bio or "Пока без описания")
            b.setObjectName("subtitle")
            b.setAlignment(Qt.AlignCenter)
            b.setWordWrap(True)
            v.addWidget(b)
            btn = QPushButton("Закрыть")
            btn.clicked.connect(self.reject)
            v.addWidget(btn)

    def pick_avatar(self):
        path, _ = QFileDialog.getOpenFileName(self, "Фото профиля", "",
                                              "Изображения (*.png *.jpg *.jpeg *.webp *.bmp)")
        if not path:
            return
        self.avatar_b64 = image_to_b64(path, 160, 85)
        self.av.set_avatar_b64(self.avatar_b64)

    def result_data(self):
        return {"display": self.name_ed.text().strip(),
                "bio": self.bio_ed.text().strip(), "avatar": self.avatar_b64}


class NoWheelComboBox(QComboBox):
    def wheelEvent(self, e):
        e.ignore()


SETTINGS_QSS = f"""
QDialog#settingsDlg {{ background: {rgba(CUR['card'], 240)}; border-radius:22px; border:1px solid {rgba(CUR['stroke'], 160)}; }}
QFrame#setHead {{ background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 {rgba(CUR['accent'], 60)}, stop:1 {rgba(CUR['accent2'], 40)}); border:1px solid {rgba(CUR['accent'], 120)}; border-radius:16px; }}
QLabel#setSec {{ color:{CUR['accent2']}; font-size:10px; font-weight:800; letter-spacing:2px; margin-top:4px; }}
QComboBox {{ background: {rgba(CUR['bubble'], 220)}; border:1px solid {rgba(CUR['stroke'], 200)}; border-radius:12px; padding:8px 12px; color:{CUR['text']}; font-size:13px; }}
QComboBox:hover {{ border:1px solid {rgba(CUR['accent'], 160)}; }}
QComboBox::drop-down {{ subcontrol-origin:padding; subcontrol-position:center right; width:26px; border:none; background:transparent; }}
QComboBox QAbstractItemView {{ background:{CUR['card']}; border:1px solid {rgba(CUR['stroke'], 255)}; border-radius:12px; padding:6px; selection-background-color:{rgba(CUR['accent'], 90)}; color:{CUR['text']}; outline:none; }}
QPushButton#profBtn {{ background: {rgba(CUR['accent'], 30)}; border:1px solid {rgba(CUR['accent'], 140)}; border-radius:14px; padding:10px; color:{CUR['accent2']}; font-weight:700; }}
QPushButton#profBtn:hover {{ background: {rgba(CUR['accent'], 60)}; }}
QPushButton#ghostBtn2 {{ background: {rgba(CUR['bubble'], 200)}; border:1px solid {rgba(CUR['stroke'], 200)}; border-radius:12px; color:{CUR['text']}; font-weight:600; }}
QPushButton#ghostBtn2:hover {{ border:1px solid {rgba(CUR['accent'], 160)}; }}
"""
class DevicesDialog(QDialog):
    def __init__(self, parent, chat):
        super().__init__(parent)
        self.chat = chat
        self.setWindowTitle("Устройства")
        self.setFixedWidth(430)
        v = QVBoxLayout(self)
        v.setContentsMargins(24, 24, 24, 24)
        v.setSpacing(10)
        t = QLabel("Устройства аккаунта")
        t.setObjectName("peerName")
        v.addWidget(t)
        sub = QLabel("Где выполнен вход и когда была активность. Лишние сессии можно завершить.")
        sub.setObjectName("subtitle")
        sub.setWordWrap(True)
        v.addWidget(sub)
        self.rows_l = QVBoxLayout()
        self.rows_l.setSpacing(8)
        v.addLayout(self.rows_l)
        self.kill_all_btn = QPushButton("Завершить все другие сессии")
        self.kill_all_btn.setObjectName("ghostBtn")
        self.kill_all_btn.clicked.connect(self.kill_all)
        v.addWidget(self.kill_all_btn)
        close = QPushButton("Закрыть")
        close.setObjectName("sendBtn")
        close.clicked.connect(self.accept)
        v.addWidget(close)
        self.sessions = []
        QTimer.singleShot(100, lambda: self.chat.send_pkt({"type": "sessions"}))
    def set_sessions(self, sessions):
        self.sessions = sessions or []
        while self.rows_l.count():
            it = self.rows_l.takeAt(0)
            w = it.widget()
            if w:
                w.deleteLater()
        for s in self.sessions:
            row = QFrame()
            row.setStyleSheet(f"background:{rgba(CUR['bubble'], 200)}; border:1px solid {rgba(CUR['stroke'], 200)}; border-radius:12px;")
            rl = QVBoxLayout(row)
            rl.setContentsMargins(12, 10, 12, 10)
            rl.setSpacing(2)
            top = QHBoxLayout()
            dev = QLabel(s.get("device") or "Неизвестное устройство")
            dev.setStyleSheet("font-weight:700; font-size:13px; background:transparent; border:none;")
            top.addWidget(dev, 1)
            if s.get("current"):
                cur = QLabel("Текущее устройство")
                cur.setStyleSheet(f"color:{CUR['online']}; font-size:11px; font-weight:700; background:transparent; border:none;")
                top.addWidget(cur)
            rl.addLayout(top)
            meta = QLabel(f"{s.get('platform') or ''} · {s.get('ip') or ''}")
            meta.setObjectName("subtitle")
            meta.setStyleSheet("background:transparent; border:none;")
            rl.addWidget(meta)
            lt = QLabel("Вход: " + _fmt_ts(s.get("login")) + (" · сейчас в сети" if s.get("current") else " · был(а): " + _fmt_ts(s.get("last"))))
            lt.setObjectName("subtitle")
            lt.setStyleSheet("background:transparent; border:none;")
            rl.addWidget(lt)
            if not s.get("current"):
                kb = QPushButton("Завершить")
                kb.setObjectName("ghostBtn")
                kb.clicked.connect(lambda _, sid=s.get("sid"): self.kill(sid))
                rl.addWidget(kb)
            self.rows_l.addWidget(row)
        if not self.sessions:
            lb = QLabel("Пока нет данных…")
            lb.setObjectName("subtitle")
            self.rows_l.addWidget(lb)
    def kill(self, sid):
        self.chat.send_pkt({"type": "session_kill", "sid": sid})
        QTimer.singleShot(700, lambda: self.chat.send_pkt({"type": "sessions"}))
    def kill_all(self):
        for s in self.sessions:
            if not s.get("current"):
                self.chat.send_pkt({"type": "session_kill", "sid": s.get("sid")})
        QTimer.singleShot(700, lambda: self.chat.send_pkt({"type": "sessions"}))

class EmailDialog(QDialog):
    def __init__(self, parent, chat):
        super().__init__(parent)
        self.chat = chat
        self.setWindowTitle("Почта для входа")
        self.setFixedWidth(360)
        v = QVBoxLayout(self)
        v.setContentsMargins(24, 24, 24, 24)
        v.setSpacing(12)
        hint = QLabel("Привяжи почту — сможешь входить кодом из письма, даже если забудешь пароль.")
        hint.setObjectName("subtitle")
        hint.setWordWrap(True)
        v.addWidget(hint)
        self.em = QLineEdit()
        self.em.setPlaceholderText("Новая почта (например, me@mail.ru)")
        v.addWidget(self.em)
        self.code = QLineEdit()
        self.code.setPlaceholderText("Код из письма")
        v.addWidget(self.code)
        self.status = QLabel("")
        self.status.setStyleSheet("color:#ff7675; font-size:12px;")
        self.status.setWordWrap(True)
        v.addWidget(self.status)
        self.btn = QPushButton("Отправить код")
        self.btn.setObjectName("sendBtn")
        self.btn.clicked.connect(self.step)
        v.addWidget(self.btn)
        self._sent = False
    def step(self):
        em = self.em.text().strip().lower()
        if not self._sent:
            if "@" not in em:
                self.status.setText("Введи корректную почту")
                return
            self.chat.send_pkt({"type": "set_email_request", "email": em})
            self.status.setStyleSheet("color:%s; font-size:12px;" % CUR["muted"])
            self.status.setText("Отправляем код…")
        else:
            cd = self.code.text().strip()
            if not cd:
                self.status.setText("Введи код из письма")
                return
            self.chat.send_pkt({"type": "set_email_confirm", "email": em, "code": cd})
    def code_sent(self):
        self._sent = True
        self.btn.setText("Привязать почту")
        self.status.setText("Код отправлен на почту ✉️")
        self.adjustSize()
    def show_err(self, msg):
        self.status.setStyleSheet("color:#ff7675; font-size:12px;")
        self.status.setText(msg or "Ошибка")
    def done_ok(self, email):
        self.chat.my_email = email or ""
        self.accept()

class SettingsDialog(QDialog):
    CATS = [("🎨", "Персонализация"), ("🔔", "Звук и уведомления"),
            ("🛡", "Безопасность"), ("🎙", "Устройства"), ("ℹ️", "О программе")]
    def __init__(self, parent, chat):
        super().__init__(parent)
        self.chat = chat
        self.setWindowTitle("Настройки")
        self.resize(640, 520)
        self.setObjectName("settingsDlg")
        self.setStyleSheet(SETTINGS_QSS +
            "QPushButton#navBtn { background: transparent; border: none; border-radius: 12px; "
            "padding: 10px 12px; text-align: left; font-size: 13px; font-weight: 600; color: " + CUR["muted"] + "; }"
            "QPushButton#navBtn:hover { background: " + rgba(CUR["hover"], 160) + "; color: " + CUR["text"] + "; }"
            "QPushButton#navBtn[sel=\"true\"] { background: " + rgba(CUR["accent"], 70) + "; color: " + CUR["text"] + "; }")
        root = QHBoxLayout(self)
        root.setContentsMargins(18, 18, 18, 18)
        root.setSpacing(14)
        nav = QVBoxLayout()
        nav.setSpacing(6)
        t = QLabel("Настройки")
        t.setObjectName("peerName")
        nav.addWidget(t)
        nav.addSpacing(8)
        self.nav_btns = []
        self.stack = QStackedWidget()
        for i, (ic, nm) in enumerate(self.CATS):
            b = QPushButton(ic + "  " + nm)
            b.setObjectName("navBtn")
            b.setCursor(Qt.PointingHandCursor)
            b.clicked.connect(lambda _, i=i: self.go(i))
            nav.addWidget(b)
            self.nav_btns.append(b)
        nav.addStretch(1)
        close = QPushButton("Закрыть")
        close.setObjectName("ghostBtn2")
        close.clicked.connect(self.accept)
        nav.addWidget(close)
        root.addLayout(nav)
        root.addWidget(self.stack, 1)
        self.stack.addWidget(self._page_personal())
        self.stack.addWidget(self._page_notify())
        self.stack.addWidget(self._page_security())
        self.stack.addWidget(self._page_devices())
        self.stack.addWidget(self._page_about())
        self.go(0)
    def go(self, i):
        self.stack.setCurrentIndex(i)
        for j, b in enumerate(self.nav_btns):
            b.setProperty("sel", "true" if j == i else "false")
            b.style().unpolish(b)
            b.style().polish(b)
    def _scroll(self):
        w = QScrollArea()
        w.setWidgetResizable(True)
        w.setStyleSheet("QScrollArea{background:transparent;border:none;}")
        inner = QWidget()
        inner.setStyleSheet("background:transparent;")
        v = QVBoxLayout(inner)
        v.setContentsMargins(4, 4, 4, 4)
        v.setSpacing(10)
        v.addStretch(1)
        w.setWidget(inner)
        return w, v
    def _row(self, v):
        fr = QFrame()
        fr.setStyleSheet("background:" + rgba(CUR["bubble"], 200) + "; border:1px solid " + rgba(CUR["stroke"], 200) + "; border-radius:12px;")
        hl = QHBoxLayout(fr)
        hl.setContentsMargins(12, 8, 12, 8)
        hl.setSpacing(10)
        v.insertWidget(v.count() - 1, fr)
        return hl
    def _sec(self, v, text):
        lb = QLabel(text.upper())
        lb.setStyleSheet("color:" + CUR["accent2"] + "; font-size:10px; font-weight:800; letter-spacing:2px; background:transparent;")
        v.insertWidget(v.count() - 1, lb)
    def _page_personal(self):
        w, v = self._scroll()
        head = QFrame()
        head.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 " + rgba(CUR["accent"], 60) + ", stop:1 " + rgba(CUR["accent2"], 40) + "); border:1px solid " + rgba(CUR["accent"], 120) + "; border-radius:16px;")
        hh = QHBoxLayout(head)
        hh.setContentsMargins(14, 12, 14, 12)
        hh.setSpacing(12)
        av = AvatarWidget(self.chat.me, 52, ring=True)
        av.set_avatar_b64(self.chat.my_profile["avatar"])
        col = QVBoxLayout()
        col.setSpacing(2)
        nm = QLabel(self.chat.my_profile["display"] or self.chat.me)
        nm.setObjectName("peerName")
        un = QLabel("@" + self.chat.me)
        un.setObjectName("subtitle")
        col.addWidget(nm)
        col.addWidget(un)
        hh.addWidget(av)
        hh.addLayout(col, 1)
        prof = QPushButton("✎")
        prof.setObjectName("ghostBtn2")
        prof.setFixedSize(34, 34)
        prof.setStyleSheet("padding:0px;")
        prof.clicked.connect(lambda: self.chat.open_my_profile())
        hh.addWidget(prof)
        v.insertWidget(v.count() - 1, head)
        self._sec(v, "Персонализация")
        cst = "QComboBox { background: " + CUR["input"] + "; border: 1px solid " + CUR["stroke"] + "; border-radius: 10px; padding: 6px 10px; color: " + CUR["text"] + "; font-size: 13px; }"
        hl = self._row(v)
        hl.addWidget(QLabel("Тема"), 1)
        self.theme_cb = NoWheelComboBox()
        self.theme_cb.setStyleSheet(cst)
        self.theme_cb.setFixedHeight(32)
        self.theme_cb.addItems(list(THEMES.keys()))
        cur_name = next((k for k, val in THEMES.items() if val == CUR), "Тёмная")
        self.theme_cb.setCurrentText(cur_name)
        self.theme_cb.currentTextChanged.connect(self.chat.apply_theme)
        hl.addWidget(self.theme_cb)
        hl = self._row(v)
        hl.addWidget(QLabel("Обои чата"), 1)
        self.wall_cb = NoWheelComboBox()
        self.wall_cb.setStyleSheet(cst)
        self.wall_cb.setFixedHeight(32)
        self.wall_cb.addItems(WALLPAPERS)
        self.wall_cb.setCurrentText(WALL)
        self.wall_cb.currentTextChanged.connect(self.chat.apply_wallpaper)
        hl.addWidget(self.wall_cb)
        hl = self._row(v)
        hl.addWidget(QLabel("Размер шрифта пузырей"), 1)
        from PySide6.QtWidgets import QSlider
        self.font_sl = QSlider(Qt.Horizontal)
        self.font_sl.setRange(10, 22)
        self.font_sl.setValue(FONT_SZ)
        self.font_sl.setFixedHeight(28)
        self.font_sl.valueChanged.connect(self._set_font_sz)
        hl.addWidget(self.font_sl, 2)
        self.font_lbl = QLabel(str(FONT_SZ))
        hl.addWidget(self.font_lbl)
        return w
    def _page_notify(self):
        w, v = self._scroll()
        self._sec(v, "Звук и уведомления")
        self.sound_cb = QCheckBox("Звук новых сообщений")
        self.sound_cb.setChecked(SOUND_ON)
        self.sound_cb.toggled.connect(self._set_sound)
        self.sound_cb.setStyleSheet("background:transparent; font-size:13px;")
        fr = QFrame()
        fr.setStyleSheet("background:" + rgba(CUR["bubble"], 200) + "; border:1px solid " + rgba(CUR["stroke"], 200) + "; border-radius:12px;")
        hl = QHBoxLayout(fr)
        hl.setContentsMargins(12, 6, 12, 6)
        hl.addWidget(self.sound_cb)
        v.insertWidget(v.count() - 1, fr)
        self.toast_cb = QCheckBox("Всплывающие уведомления (тосты)")
        self.toast_cb.setChecked(TOASTS_ON)
        self.toast_cb.toggled.connect(self._set_toasts)
        self.toast_cb.setStyleSheet("background:transparent; font-size:13px;")
        fr = QFrame()
        fr.setStyleSheet("background:" + rgba(CUR["bubble"], 200) + "; border:1px solid " + rgba(CUR["stroke"], 200) + "; border-radius:12px;")
        hl = QHBoxLayout(fr)
        hl.setContentsMargins(12, 6, 12, 6)
        hl.addWidget(self.toast_cb)
        v.insertWidget(v.count() - 1, fr)
        return w
    def _page_security(self):
        w, v = self._scroll()
        self._sec(v, "Безопасность")
        lock_btn = QPushButton("🔒 Код-пароль")
        lock_btn.setObjectName("ghostBtn2")
        lock_btn.setFixedHeight(38)
        lock_btn.clicked.connect(lambda: LockDialog(self).exec())
        v.insertWidget(v.count() - 1, lock_btn)
        em_row = self._row(v)
        em_row.addWidget(QLabel("Почта для входа"), 1)
        self.email_lbl = QLabel(getattr(self.chat, "my_email", "") or "не привязана")
        self.email_lbl.setObjectName("subtitle")
        em_row.addWidget(self.email_lbl)
        em_btn = QPushButton("Изменить")
        em_btn.setObjectName("ghostBtn2")
        em_btn.clicked.connect(self.open_email)
        em_row.addWidget(em_btn)
        dev_btn = QPushButton("🖥 Устройства аккаунта")
        dev_btn.setObjectName("sendBtn")
        dev_btn.setFixedHeight(38)
        dev_btn.clicked.connect(self.open_devices)
        v.insertWidget(v.count() - 1, dev_btn)
        hint = QLabel("Код-пароль закрывает чаты на этом устройстве, а список устройств показывает все активные входы в аккаунт.")
        hint.setObjectName("subtitle")
        hint.setWordWrap(True)
        v.insertWidget(v.count() - 1, hint)
        return w
    def _page_devices(self):
        w, v = self._scroll()
        self._sec(v, "Устройства")
        cst = "QComboBox { background: " + CUR["input"] + "; border: 1px solid " + CUR["stroke"] + "; border-radius: 10px; padding: 6px 10px; color: " + CUR["text"] + "; font-size: 13px; }"
        mics, cams = self.chat.device_lists()
        hl = self._row(v)
        hl.addWidget(QLabel("Микрофон"), 1)
        self.mic_cb = NoWheelComboBox()
        self.mic_cb.setStyleSheet(cst)
        self.mic_cb.setFixedHeight(32)
        if mics:
            for i, name in mics:
                self.mic_cb.addItem(name, i)
        else:
            self.mic_cb.addItem("По умолчанию", -1)
        idx = self.mic_cb.findData(MIC_DEV)
        if idx >= 0:
            self.mic_cb.setCurrentIndex(idx)
        self.mic_cb.currentIndexChanged.connect(lambda: self.chat.apply_devices(mic=self.mic_cb.currentData()))
        hl.addWidget(self.mic_cb)
        hl = self._row(v)
        hl.addWidget(QLabel("Камера"), 1)
        self.cam_cb = NoWheelComboBox()
        self.cam_cb.setStyleSheet(cst)
        self.cam_cb.setFixedHeight(32)
        if cams:
            for i, name in cams:
                self.cam_cb.addItem(name, i)
        else:
            self.cam_cb.addItem("Не найдена", -1)
        idx = self.cam_cb.findData(CAM_DEV)
        if idx >= 0:
            self.cam_cb.setCurrentIndex(idx)
        self.cam_cb.currentIndexChanged.connect(lambda: self.chat.apply_devices(cam=self.cam_cb.currentData()))
        hl.addWidget(self.cam_cb)
        return w
    def _page_about(self):
        w, v = self._scroll()
        lb = QLabel(APP_NAME + " · версия 7.2\nответы · правки · пересылка · избранное · файлы\nреакции · опросы · истории · звонки · сессии")
        lb.setObjectName("subtitle")
        lb.setAlignment(Qt.AlignCenter)
        lb.setWordWrap(True)
        v.insertWidget(v.count() - 1, lb)
        return w
    def _set_font_sz(self, v):
        global FONT_SZ
        FONT_SZ = int(v)
        try:
            self.font_lbl.setText(str(v))
        except Exception:
            pass
        save_extra()
        try:
            ch = self.chat
            if ch.peer and ch.cache.get(ch.peer):
                ch.clear_messages()
                for m in ch.cache.get(ch.peer, []):
                    ch._render_cached(ch.peer, m)
                ch.scroll_to_bottom()
        except Exception:
            pass

    def open_email(self):
        app = getattr(self.chat, "app", None)
        dlg = EmailDialog(self, self.chat)
        if app is not None:
            app.email_dlg = dlg
        dlg.exec()
        if app is not None:
            app.email_dlg = None
        try:
            self.email_lbl.setText(getattr(self.chat, "my_email", "") or "не привязана")
        except Exception:
            pass

    def _set_sound(self, on):
        global SOUND_ON
        SOUND_ON = bool(on)
        save_settings()
    def _set_toasts(self, on):
        global TOASTS_ON
        TOASTS_ON = bool(on)
        save_settings()
    def open_devices(self):
        app = getattr(self.chat, "app", None)
        dlg = DevicesDialog(self, self.chat)
        if app is not None:
            app.devices_dlg = dlg
        dlg.exec()
        if app is not None:
            app.devices_dlg = None

class LockScreen(QWidget):
    unlocked = Signal()
    forgot = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.card = QFrame(self)
        self.card.setAttribute(Qt.WA_StyledBackground, True)
        self.card.setObjectName("card")
        self.card.setFixedWidth(360)
        v = QVBoxLayout(self.card)
        v.setContentsMargins(30, 26, 30, 24)
        v.setSpacing(12)
        ic = IconBtn("lock", 64)
        ic.setEnabled(False)
        v.addWidget(ic, 0, Qt.AlignHCenter)
        t = QLabel("Bebsi заблокирован")
        t.setObjectName("title")
        t.setAlignment(Qt.AlignCenter)
        v.addWidget(t)
        self.code = QLineEdit()
        self.code.setPlaceholderText("Код-пароль")
        self.code.setEchoMode(QLineEdit.Password)
        self.code.setAlignment(Qt.AlignCenter)
        self.code.returnPressed.connect(self.try_unlock)
        v.addWidget(self.code)
        self.btn = QPushButton("Разблокировать")
        self.btn.setMinimumHeight(38)
        self.btn.clicked.connect(self.try_unlock)
        v.addWidget(self.btn)
        self.forgot_btn = QPushButton("Забыл код? Выйти")
        self.forgot_btn.setObjectName("ghostBtn")
        self.forgot_btn.setMinimumHeight(34)
        self.forgot_btn.clicked.connect(self.forgot.emit)
        v.addWidget(self.forgot_btn)
        fh = QLabel("Выход без кода сбросит код-пароль и сохранённые аккаунты — придётся войти заново")
        fh.setObjectName("subtitle")
        fh.setWordWrap(True)
        fh.setAlignment(Qt.AlignCenter)
        v.addWidget(fh)
        self.status = QLabel("")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("color:#ff7675; font-size:12px;")
        v.addWidget(self.status)
        self.card.adjustSize()
    def showEvent(self, e):
        super().showEvent(e)
        self.code.setText("")
        self.status.setText("")
        QTimer.singleShot(150, self.code.setFocus)
        self.center_card()
    def center_card(self):
        self.card.adjustSize()
        self.card.move((self.width() - self.card.width()) // 2,
                       max(24, (self.height() - self.card.height()) // 2))
    def try_unlock(self):
        if lock_hash(self.code.text()) == LOCK_HASH:
            self.unlocked.emit()
        else:
            self.status.setText("Неверный код 🔒")
            self.code.setText("")
            self.code.setFocus()
class LockDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Код-пароль")
        self.setFixedWidth(340)
        v = QVBoxLayout(self)
        v.setContentsMargins(24, 24, 24, 24)
        v.setSpacing(12)
        hint = QLabel("Код-пароль закрывает доступ к чатам. Замочек в сайдбаре блокирует мгновенно.")
        hint.setObjectName("subtitle")
        hint.setWordWrap(True)
        v.addWidget(hint)
        self.cur = None
        if LOCK_HASH:
            self.cur = QLineEdit()
            self.cur.setPlaceholderText("Текущий код")
            self.cur.setEchoMode(QLineEdit.Password)
            v.addWidget(self.cur)
        self.n1 = QLineEdit()
        self.n1.setPlaceholderText("Новый код (минимум 4 символа)")
        self.n1.setEchoMode(QLineEdit.Password)
        v.addWidget(self.n1)
        self.n2 = QLineEdit()
        self.n2.setPlaceholderText("Повтори новый код")
        self.n2.setEchoMode(QLineEdit.Password)
        v.addWidget(self.n2)
        self.status = QLabel("")
        self.status.setStyleSheet("color:#ff7675; font-size:12px;")
        self.status.setWordWrap(True)
        v.addWidget(self.status)
        row = QHBoxLayout()
        if LOCK_HASH:
            off = QPushButton("Выключить")
            off.setObjectName("ghostBtn")
            off.clicked.connect(self.disable)
            row.addWidget(off)
        row.addStretch(1)
        ok = QPushButton("Сохранить")
        ok.setObjectName("sendBtn")
        ok.clicked.connect(self.save)
        row.addWidget(ok)
        bw = QWidget(); bw.setLayout(row)
        v.addWidget(bw)
    def save(self):
        global LOCK_HASH
        if self.cur is not None and lock_hash(self.cur.text()) != LOCK_HASH:
            self.status.setText("Текущий код неверный")
            return
        c1, c2 = self.n1.text(), self.n2.text()
        if len(c1) < 4:
            self.status.setText("Минимум 4 символа")
            return
        if c1 != c2:
            self.status.setText("Коды не совпадают")
            return
        LOCK_HASH = lock_hash(c1)
        save_settings()
        self.accept()
    def disable(self):
        global LOCK_HASH
        if self.cur is not None and lock_hash(self.cur.text()) != LOCK_HASH:
            self.status.setText("Текущий код неверный")
            return
        LOCK_HASH = ""
        save_settings()
        self.accept()
class ChatPane(QFrame):
    def paintEvent(self, e):
        return


# ================== ЭКРАН ВХОДА ==================

class AuthScreen(QWidget):
    submit = Signal(str, str, str)
    code_req = Signal(str)
    email_sub = Signal(str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mode = "login"
        self._entered = False
        self.card = QFrame(self)
        self.card.setAttribute(Qt.WA_StyledBackground, True)
        self.card.setObjectName("card")
        self.card.setFixedSize(380, 480)
        v = QVBoxLayout(self.card)
        v.setContentsMargins(34, 30, 34, 26)
        v.setSpacing(0)
        top = QHBoxLayout()
        top.setSpacing(12)
        top.addWidget(AvatarWidget(APP_NAME, 46))
        title = QLabel(APP_NAME)
        title.setObjectName("title")
        top.addWidget(title)
        top.addStretch(1)
        v.addLayout(top)
        v.addSpacing(6)
        sub = QLabel(APP_SUBTITLE)
        sub.setObjectName("subtitle")
        v.addWidget(sub)
        v.addSpacing(26)
        self.u = QLineEdit()
        self.u.setPlaceholderText("Имя пользователя")
        self.p = QLineEdit()
        self.p.setPlaceholderText("Пароль (минимум 4 символа)")
        self.p.setEchoMode(QLineEdit.Password)
        v.addWidget(self.u)
        v.addSpacing(10)
        v.addWidget(self.p)
        self.e = QLineEdit()
        self.e.setPlaceholderText("Почта (необязательно, для входа кодом)")
        self.e.hide()
        v.addWidget(self.e)
        v.addSpacing(18)
        self.btn = QPushButton("Войти")
        self.btn.clicked.connect(self.do_submit)
        v.addWidget(self.btn)
        v.addSpacing(12)
        self.toggle = QPushButton("Нет аккаунта? Создать")
        self.toggle.setObjectName("ghostBtn")
        self.toggle.clicked.connect(self.flip)
        v.addWidget(self.toggle, 0, Qt.AlignHCenter)
        self.em_btn = QPushButton("✉️ Вход по почте")
        self.em_btn.setObjectName("ghostBtn")
        self.em_btn.clicked.connect(self.toggle_email)
        v.addWidget(self.em_btn, 0, Qt.AlignHCenter)
        v.addStretch(1)
        self.status = QLabel(APP_NAME)
        self.status.setAlignment(Qt.AlignHCenter)
        self.status.setWordWrap(True)
        v.addWidget(self.status)
        self.p.returnPressed.connect(self.do_submit)
        self.p.textChanged.connect(self._upd_btn)
        self.u.returnPressed.connect(lambda: self.p.setFocus())
        self._anim_t = QTimer(self)
        self._anim_t.setInterval(50)
        self._anim_t.timeout.connect(self.update)
        self._anim_t.start()

    def flip(self):
        self.mode = "register" if self.mode == "login" else "login"
        self.e.setVisible(self.mode == "register")
        if self.mode == "login":
            self.btn.setText("Войти")
            self.toggle.setText("Нет аккаунта? Создать")
        else:
            self.btn.setText("Создать аккаунт")
            self.toggle.setText("Уже есть аккаунт? Войти")
        self.status.setText("")

    def _upd_btn(self, txt=None):
        if getattr(self, "email_mode", False):
            self.btn.setText("Войти" if self.p.text().strip() else "Получить код")

    def toggle_email(self):
        self.email_mode = not getattr(self, "email_mode", False)
        self._code_sent = False
        self.e.hide()
        if self.email_mode:
            self.u.setPlaceholderText("Электронная почта")
            self.p.setPlaceholderText("Код из письма")
            self.p.setEchoMode(QLineEdit.Normal)
            self.btn.setText("Получить код")
            self.status.setText("")
        else:
            self.u.setPlaceholderText("Имя пользователя")
            self.p.setPlaceholderText("Пароль (минимум 4 символа)")
            self.p.setEchoMode(QLineEdit.Password)
            self.btn.setText("Войти")
            self.status.setText("")

    def code_step(self):
        self._code_sent = True
        self.btn.setText("Войти")
        self.set_status("Код отправлен на почту ✉️")

    def do_submit(self):
        u, p = self.u.text().strip(), self.p.text()
        if getattr(self, "email_mode", False):
            if "@" not in u:
                self.error("Введи корректную почту")
                return
            if p.strip():
                self.submit.emit("email_login", u, p.strip())
                self._arm_splash()
            else:
                self.submit.emit("email_code", u, "")
                self.set_status("Отправляем код…")
            return

        if not u:
            self.error("Введите имя")
            return
        if self.mode == "register" and len(p) < 6:
            self.error("Пароль для регистрации — минимум 6 символов")
            return
        if len(p) < 4:
            self.error("Пароль должен быть не короче 4 символов")
            return
        self.submit.emit(self.mode, u, p)
        self._arm_splash()

    def error(self, msg):
        if getattr(self, "_splash_t", None) is not None:
            self._splash_t.stop()
        self.status.setStyleSheet("color:#ff7675; font-size:12px;")
        self.status.setText(msg)

    def set_status(self, msg):
        self.status.setStyleSheet(f"color:{CUR['muted']}; font-size:12px;")
        self.status.setText(msg)

    def reset(self):
        self.u.clear()
        self.p.clear()
        self.status.setText("")
        if self.mode != "login":
            self.flip()

    def enter_anim(self):
        self.center_card()
        eff = QGraphicsOpacityEffect(self.card)
        self.card.setGraphicsEffect(eff)
        x, y = self.card.x(), self.card.y()
        a1 = QPropertyAnimation(self.card, b"pos")
        a1.setDuration(650)
        a1.setStartValue(QPoint(x, y + 36))
        a1.setEndValue(QPoint(x, y))
        a1.setEasingCurve(QEasingCurve.OutExpo)
        a2 = QPropertyAnimation(eff, b"opacity")
        a2.setDuration(500)
        a2.setStartValue(0.0)
        a2.setEndValue(1.0)
        grp = QParallelAnimationGroup(self)
        grp.addAnimation(a1)
        grp.addAnimation(a2)
        grp.finished.connect(lambda: self.card.setGraphicsEffect(None))
        self._anim = grp
        grp.start()

    def shake(self):
        x, y = self.card.x(), self.card.y()
        a = QPropertyAnimation(self.card, b"pos")
        a.setDuration(400)
        for t, dx in ((0, 0), (0.2, -12), (0.4, 10), (0.6, -6), (0.8, 4), (1, 0)):
            a.setKeyValueAt(t, QPoint(x + dx, y))
        self._shake = a
        a.start()

    def center_card(self):
        self.card.move((self.width() - self.card.width()) // 2,
                       max(24, (self.height() - self.card.height()) // 2))

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, "card"):
            self.center_card()

    def showEvent(self, e):
        super().showEvent(e)
        if not self._entered:
            self._entered = True
            self.enter_anim()

    def paintEvent(self, _):
        import math as _m
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        T = time.time()
        g = QLinearGradient(0, 0, 0, self.height())
        g.setColorAt(0, QColor(CUR["bg"]))
        g.setColorAt(1, QColor(CUR["bg"]).darker(116 if not _is_light() else 106))
        p.fillRect(self.rect(), QBrush(g))
        p.setPen(Qt.NoPen)
        for i, col in enumerate(("#7c5cff", "#22d3ee", "#ff5e7d")):
            c = QColor(col); c.setAlpha(46)
            cx = self.width() * (0.5 + 0.40 * _m.sin(T * 0.13 + i * 2.0))
            cy = self.height() * (0.5 + 0.38 * _m.cos(T * 0.10 + i * 1.6))
            r = max(self.width(), self.height()) * 0.42
            rg = QRadialGradient(cx, cy, r)
            rg.setColorAt(0, c)
            c0 = QColor(col); c0.setAlpha(0)
            rg.setColorAt(1, c0)
            p.setBrush(QBrush(rg))
            p.drawEllipse(QPointF(cx, cy), r, r)
        for i in range(60):
            sx = (i * 97.3) % self.width()
            sy = (self.height() + 40 - ((T * (8 + (i % 6) * 4) + i * 53) % (self.height() + 80)))
            c = QColor("#ffffff" if not _is_light() else CUR["text"]); c.setAlpha(30 + int(28 * _m.sin(T * 1.5 + i)))
            p.setBrush(c)
            p.drawEllipse(QPointF(sx, sy), 1.4 + (i % 3), 1.4 + (i % 3))
        gc = QColor("#ffffff" if not _is_light() else CUR["text"]); gc.setAlpha(10 if not _is_light() else 14)
        p.setPen(QPen(gc, 1))
        x = 0
        while x < self.width():
            p.drawLine(x, 0, x, self.height())
            x += 46
        y = 0
        while y < self.height():
            p.drawLine(0, y, self.width(), y)
            y += 46
        p.setPen(Qt.NoPen)

# ================== ЭКРАН ЧАТА ==================

class ForwardDialog(QDialog):
    def __init__(self, parent, targets):
        super().__init__(parent)
        self.setWindowTitle(" Переслать")
        self.setFixedWidth(300)
        self.result_key = None
        v = QVBoxLayout(self)
        v.setSpacing(8)
        for key, disp in targets:
            b = QPushButton(disp)
            b.setObjectName("ghostBtn")
            b.clicked.connect(lambda _, k=key: self.pick(k))
            v.addWidget(b)

    def pick(self, k):
        self.result_key = k
        self.accept()


TOASTS = []

class Toast(QWidget):
    clicked = Signal(str)

    def __init__(self, title, text, key, parent=None):
        super().__init__(parent)
        self.key = key
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)
        self.setObjectName("Toast")
        h = QHBoxLayout(self)
        h.setContentsMargins(12, 10, 12, 10)
        h.setSpacing(10)
        av = QLabel((title or "?")[:1].upper())
        av.setFixedSize(38, 38)
        av.setAlignment(Qt.AlignCenter)
        av.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 #8b5cf6, stop:1 #22d3ee); border-radius: 12px; color: white; font-size: 15px; font-weight: 800; border: 1px solid rgba(255,255,255,0.25);")
        col = QVBoxLayout()
        col.setSpacing(2)
        app_lbl = QLabel("BEBSI  ·  новое сообщение")
        app_lbl.setStyleSheet("color: #22d3ee; font-size: 10px; font-weight: 800; letter-spacing: 2px; background: transparent;")
        col.addWidget(app_lbl)
        tl = QLabel(title or "")
        tl.setStyleSheet("color: #f4f4ff; font-size: 13px; font-weight: 700; background: transparent;")
        bd = QLabel(text or "")
        bd.setWordWrap(True)
        bd.setMaximumWidth(250)
        bd.setStyleSheet("color: #aab0d0; font-size: 12px; background: transparent;")
        col.addWidget(tl)
        col.addWidget(bd)
        h.addWidget(av)
        h.addLayout(col)
        self.setStyleSheet("#Toast { background: rgba(16,18,34,0.90); border-radius: 18px; border: 1px solid rgba(139,92,246,0.40); }")

    def pop(self):
        try:
            scr = QApplication.primaryScreen().availableGeometry()
        except Exception:
            scr = None
        self.adjustSize()
        if scr is not None:
            y = scr.bottom() - self.height() - 48 - len(TOASTS) * (self.height() + 10)
            self.move(scr.right() - self.width() + 80, y)
        self.show()
        TOASTS.append(self)
        if len(TOASTS) > 4:
            TOASTS[0].bye()
        self._eff = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._eff)
        self._a = QPropertyAnimation(self._eff, b"opacity", self)
        self._a.setDuration(220)
        self._a.setStartValue(0.0)
        self._a.setEndValue(1.0)
        self._a.start()
        if scr is not None:
            self._g = QPropertyAnimation(self, b"pos", self)
            self._g.setDuration(220)
            self._g.setStartValue(self.pos())
            self._g.setEndValue(QPoint(scr.right() - self.width() - 12, self.y()))
            self._g.start()
        QTimer.singleShot(4200, self.bye)

    def bye(self):
        try:
            if self in TOASTS:
                TOASTS.remove(self)
            self._b = QPropertyAnimation(self._eff, b"opacity", self)
            self._b.setDuration(180)
            self._b.setStartValue(1.0)
            self._b.setEndValue(0.0)
            self._b.finished.connect(self.close)
            self._b.start()
        except Exception:
            self.close()

    def mousePressEvent(self, e):
        self.clicked.emit(self.key)
        self.bye()


class ChatScreen(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.me = None
        self.peer = None
        self.chats = {}
        self.items = {}
        self.my_bubbles = {}
        self.bubbles_by_id = {}
        self.my_profile = {"display": "", "bio": "", "avatar": ""}
        self.story_data = {}
        self.cache = {}
        self.recorder = None
        self.circle_rec = None
        self.circle_dlg = None
        self.reply_info = None
        self.edit_mid = None
        self.last_seen = {}
        self._last_typing_sent = 0.0
        self._splashed = False
        self._missed = 0
        self._missed = 0
        self.setAcceptDrops(True)

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)
        self.upd_banner = self.build_upd_banner()
        outer.addWidget(self.upd_banner)
        root = QHBoxLayout()
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)
        root.addWidget(self.build_sidebar())
        root.addWidget(self.build_chat(), 1)
        outer.addLayout(root, 1)
        self._set_input_vis(False)

        self.upd_timer = QTimer(self)
        self.upd_timer.setInterval(30000)
        self.upd_timer.timeout.connect(self._check_upd)
        self.upd_timer.start()
        self.typing_timer = QTimer(self)
        self.typing_timer.setSingleShot(True)
        self.typing_timer.timeout.connect(self.hide_typing)

        self.rec_timer = QTimer(self)
        self.rec_timer.setInterval(1000)
        self.rec_timer.timeout.connect(self.tick_rec)
        self.rec_sec = 0
        self.warn_timer = QTimer(self)
        self.warn_timer.setSingleShot(True)
        self.warn_timer.setInterval(4000)
        self.warn_timer.timeout.connect(self._clear_warn)
        self.pres_t = QTimer(self)
        self.pres_t.setInterval(15000)
        self.pres_t.timeout.connect(self._pres_poll)
        self.pres_t.start()
        self._down_t = QTimer(self)
        self._down_t.setInterval(300)
        self._down_t.timeout.connect(lambda: self._safe_down())
        self._down_t.start()
        self._sched_t = QTimer(self)
        self._sched_t.setInterval(5000)
        self._sched_t.timeout.connect(self._sched_tick)
        self._sched_t.start()

    def open_chat_menu(self, name, pos):
        global DND_ON
        menu = QMenu(self)
        menu.setStyleSheet(f"QMenu{{background:{CUR['bg']}; color:{CUR['text']}; border:1px solid {CUR['stroke']}; border-radius:8px;}} QMenu::item{{padding:6px 18px; border-radius:6px;}} QMenu::item:selected{{background:{CUR['accent']};}}")
        is_grp = str(name).startswith("g") and str(name)[1:].isdigit()
        is_chan = str(name).startswith("c") and str(name)[1:].isdigit()
        a_sub = None
        a_contact = None
        a_block = None
        if not is_grp and not is_chan:
            a_contact = menu.addAction("✓ В контактах" if name in CONTACTS else "👤 Добавить в контакты")
            a_block = menu.addAction("✅ Разблокировать" if name in BLOCKED else "🚫 Заблокировать")
        a_pin = menu.addAction("📌 Открепить" if name in PINNED else "📌 Закрепить")
        a_exp = menu.addAction("💾 Экспорт чата")
        a_del = menu.addAction("🗑 Удалить чат")
        a_mute = menu.addAction("🔇 Без звука" if name in MUTES else "🔊 Со звуком")
        a_dnd = menu.addAction("🌙 DND: выкл" if not DND_ON else "🌙 DND: вкл")
        a_arch = menu.addAction("🗄 Убрать в архив" if name not in ARCH else "🗄 Вернуть из архива")
        a_snz = menu.addAction("😴 Сноуз до утра" if not (SNOOZE.get(name) or "") else "😴 Разбудить")
        if is_chan:
            _cc = self.chats.get(name, {})
            a_sub = menu.addAction("➖ Отписаться" if self.me in (_cc.get("members") or []) else "➕ Подписаться")
            a_set = menu.addAction("⚙ Настройки канала") if _cc.get("owner") == self.me else None
        sub_w = menu.addMenu("🖼 Обои этого чата")
        wall_acts = {}
        for _wn in WALLPAPERS:
            _a = sub_w.addAction(_wn + (" ✓" if WALLS.get(name, WALL) == _wn else ""))
            wall_acts[_a] = _wn
        act = menu.exec(pos)
        if act is None:
            return
        if act == a_contact:
            if name in CONTACTS:
                CONTACTS.discard(name)
                self.show_warn("Убран из контактов")
            else:
                from PySide6.QtWidgets import QInputDialog


                txt, ok = QInputDialog.getText(self, "Контакт", "Имя контакта:", text=name)
                if ok and txt.strip():
                    CONTACTS.add(name)
                    CONTACT_NAMES[name] = txt.strip()
                    it = self.items.get(name)
                    if it:
                        it.set_display(txt.strip())
                        if getattr(self, "open_key", None) == name: self.peer_name.setText(txt.strip())
                    self.show_warn("Добавлен в контакты ⭐")
                    save_extra()
        elif act == a_block:
            it = self.items.get(name)
            if name in BLOCKED:
                BLOCKED.discard(name)
                if it:
                    it.set_display(name)
                if self.peer == name:
                    self.input.setEnabled(True)
            else:
                BLOCKED.add(name)
                if it:
                    it.set_display("🚫 " + name)
                if self.peer == name:
                    self.peer = None
                    self.input.setEnabled(False)
            save_extra()
        elif act == a_pin:
            if name in PINNED:
                PINNED.discard(name)
            else:
                PINNED.add(name)
            save_extra()
            self.refresh_order()
        elif act == a_exp:
            self.export_chat(name)
        elif act == a_del:
            DELETED.add(name)
            it = self.items.get(name)
            if it:
                it.hide()
            self.cache.pop(name, None)
            if self.peer == name:
                self.close_chat()
            save_extra()
            self.show_warn("Чат удалён 🗑")
        elif act == a_mute:
         if name in MUTES:
          MUTES.discard(name)
         else:
          MUTES.add(name)
         save_extra()
         self.show_warn("Звук выключен 🔇" if name in MUTES else "Звук включён 🔊")
        elif act == a_dnd:
         DND_ON = not DND_ON
         save_extra()
         self.show_warn("DND: вкл 🌙" if DND_ON else "DND: выкл")
        elif act in wall_acts:
         WALLS[name] = wall_acts[act]
         save_extra()
         self.pane.update()
         try:
             self.window().update()
         except Exception:
             pass
         self.show_warn("Обои чата: " + wall_acts[act])

        if a_sub is not None and act == a_sub:
            _cc = self.chats.get(name, {})
            _on = self.me not in (_cc.get("members") or [])
            self.send_pkt({"type": "channel_sub", "id": int(str(name)[1:]), "on": _on})
            self.show_warn("Подписка обновлена 📢")
            if act == a_arch:
                if name in ARCH:
                    ARCH.discard(name)
                else:
                    ARCH.add(name)
                _save_pack2()
                self.refresh_order()
                self.show_warn("Архив обновлён 🗄")
            if act == a_snz:
                if SNOOZE.get(name):
                    SNOOZE.pop(name, None)
                else:
                    nt = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
                    if nt <= datetime.now():
                        nt = nt + timedelta(days=1)
                    SNOOZE[name] = nt.isoformat(timespec="seconds")
                _save_pack2()
                self.refresh_order()
                self.show_warn("Сноуз до утра 😴" if SNOOZE.get(name) else "Чат активен ☀")
            if is_chan and act is not None and act.text().startswith("⚙ Настройки"):
                ChannelSettingsDialog(self, name).exec()
        
    def export_chat(self, name):
        try:
            msgs = self.cache.get(name) or []
            if not msgs:
                self.show_warn("Нет сообщений для экспорта")
                return
            path, _ = QFileDialog.getSaveFileName(self, "Экспорт чата", "chat_" + str(name) + ".txt", "Текст (*.txt);;HTML (*.html)")
            if not path:
                return
            disp = self.chats.get(name, {}).get("display", name)
            if path.lower().endswith(".html"):
                rows = "".join(f"<p><b>{m.get('sender') or ('Вы' if m.get('mine') else name)}</b> <i>{(m.get('ts') or '')[11:16]}</i>: {m.get('text') or '[вложение]'}</p>" for m in msgs)
                data = f"<html><head><meta charset='utf-8'></head><body><h2>{disp}</h2>{rows}</body></html>"
            else:
                data = "\n".join(f"{(m.get('ts') or '')[:16]}  {m.get('sender') or ('Вы' if m.get('mine') else name)}: {m.get('text') or '[вложение]'}" for m in msgs)
            with open(path, "w", encoding="utf-8") as f:
                f.write(data)
            self.show_warn("Экспорт готов 💾")
        except Exception:
            pass
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()
    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()
    def dropEvent(self, e):
        if not self.peer:
            self.show_warn("Сначала выбери чат 👈")
            return
        for url in e.mimeData().urls():
            path = url.toLocalFile()
            if not path or not os.path.exists(path):
                continue
            if path.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp")):
                b64 = image_to_b64(path, 1200, 82)
                if b64:
                    self.send_to(self.peer, media=b64, last="📷 Фото")
            else:
                if os.path.getsize(path) > 6_000_000:
                    self.show_warn("Файл больше 6 МБ 😅")
                    continue
                with open(path, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()
                self.send_to(self.peer, file_name=os.path.basename(path), file_data=b64, last="📄 Файл")
        e.acceptProposedAction()
    def find_next(self):
        try:
            q = self.find_ed.text().strip().lower()
            if not q or not self.peer:
                return
            msgs = (self.cache.get(self.peer) or [])[-300:]
            idxs = [i for i, m in enumerate(msgs) if q in (m.get("text") or "").lower()]
            if not idxs:
                self.show_warn("Не нашлось 🔎")
                return
            self._find_idx = (self._find_idx + 1) % len(idxs)
            rows = []
            for i2 in range(self.msg_l.count()):
                it = self.msg_l.itemAt(i2)
                if it is not None and it.widget():
                    rows.append(it.widget())
            t = idxs[self._find_idx]
            if t < len(rows):
                self.scroll.ensureWidgetVisible(rows[t], 50, 50)
                fade_in(rows[t], 250)
        except Exception:
            pass
    def open_contacts(self):
        from PySide6.QtWidgets import QInputDialog, QListWidget


        dlg = QDialog(self)
        dlg.setWindowTitle("Контакты")
        dlg.setStyleSheet(f"background:{CUR['bg']};")
        dlg.resize(340, 420)
        v = QVBoxLayout(dlg)
        lst = QListWidget()
        lst.setStyleSheet(f"background:{CUR['bg']}; color:{CUR['text']}; border:1px solid {CUR['stroke']}; border-radius:8px; font-size:14px;")
        for un in sorted(CONTACTS):
            lst.addItem(f"{CONTACT_NAMES.get(un, un)}  ({un})")
        v.addWidget(lst)
        row = QHBoxLayout()
        add_b = QPushButton("➕ Добавить")
        del_b = QPushButton("🗑 Убрать")
        row.addWidget(add_b)
        row.addWidget(del_b)
        bw = QWidget(); bw.setLayout(row)
        v.addWidget(bw)

        def do_add():
            un, ok = QInputDialog.getText(dlg, "Новый контакт", "Имя пользователя:")
            if not ok or not un.strip():
                return
            un = un.strip()
            nm, ok = QInputDialog.getText(dlg, "Новый контакт", "Имя в книжке:", text=un)
            nm = nm.strip() if ok and nm.strip() else un
            CONTACTS.add(un)
            CONTACT_NAMES[un] = nm
            save_extra()
            it = self.items.get(un)
            if it:
                it.set_display(nm)
                it.show()
            dlg.accept()
            self.show_warn("Контакт сохранён ⭐")

        def do_del():
            r = lst.currentRow()
            if r < 0:
                return
            un = sorted(CONTACTS)[r]
            CONTACTS.discard(un)
            CONTACT_NAMES.pop(un, None)
            save_extra()
            it = self.items.get(un)
            if it:
                it.set_display(un)
            dlg.accept()

        add_b.clicked.connect(do_add)
        del_b.clicked.connect(do_del)
        fade_in(dlg, 200)
        dlg.exec()

    def showEvent(self, e):
        super().showEvent(e)
        if not getattr(self, "_splashed", False):
            self._splashed = True


    def build_sidebar(self):
        side = QFrame()
        side.setAttribute(Qt.WA_StyledBackground, True)
        side.setObjectName("sidebar")
        side.setFixedWidth(300)
        v = QVBoxLayout(side)
        v.setContentsMargins(14, 14, 14, 14)
        v.setSpacing(10)
        top = QHBoxLayout()
        top.setSpacing(10)
        self.menu_btn = QPushButton("☰")
        self.menu_btn.setObjectName("toolBtn")
        self.menu_btn.setFixedSize(34, 34)
        self.menu_btn.setToolTip("Меню")
        self.menu_btn.clicked.connect(self.toggle_drawer)
        top.addWidget(self.menu_btn)
        t = QLabel(APP_NAME)
        t.setObjectName("title")
        top.addWidget(t)
        top.addStretch(1)
        v.addLayout(top)
        self.folder_bar = QHBoxLayout()
        self.folder_bar.setSpacing(6)
        self._folder_btns = {}
        for fid, lbl in (("all", "Все"), ("personal", "Личные"), ("groups", "Группы"), ("unread", "Непрочит.")):
            fb = QPushButton(lbl)
            fb.setObjectName("chipBtn")
            fb.setCursor(Qt.PointingHandCursor)
            fb.setProperty("mine", "true" if fid == "all" else "false")
            fb.clicked.connect(lambda _, f=fid: self.set_folder(f))
            self.folder_bar.addWidget(fb)
            self._folder_btns[fid] = fb
        self.folder_bar.addStretch(1)
        v.addLayout(self.folder_bar)
        self.folder = "all"

        self.story_scroll = QScrollArea()
        self.story_scroll.setFixedHeight(96)
        self.story_scroll.setWidgetResizable(True)
        self.story_w = QWidget()
        self.story_l = QHBoxLayout(self.story_w)
        self.story_l.setContentsMargins(4, 4, 4, 4)
        self.story_l.setSpacing(12)
        self.story_l.addStretch(1)
        self.story_scroll.setWidget(self.story_w)
        v.addWidget(self.story_scroll)
        self.story_scroll.setVisible(False)

        self.search = QLineEdit()
        self.search.textChanged.connect(self._on_search)
        self.search.setPlaceholderText("Поиск...")
        self.search.textChanged.connect(lambda: self.refresh_order())
        v.addWidget(self.search)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self.list_w = QWidget()
        self.list_l = QVBoxLayout(self.list_w)
        self.list_l.setContentsMargins(2, 2, 2, 2)
        self.list_l.setSpacing(4)
        self.list_l.addStretch(1)
        scroll.setWidget(self.list_w)
        v.addWidget(scroll, 1)

        line = QFrame()
        line.setObjectName("sepLine")
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet(f"background:{rgba(CUR['stroke'], 255)}; max-height:1px; border:none;")
        v.addWidget(line)

        me_row = QHBoxLayout()
        me_row.setSpacing(10)
        self.me_avatar = AvatarWidget("?", 38, show_dot=True, clickable=True)
        self.me_avatar.setToolTip("Мой профиль")
        self.me_avatar.clicked.connect(self.open_my_profile)
        self.me_avatar.set_online(True)
        self.me_name = QLabel("…")
        self.me_name.setObjectName("itemName")
        self.acc_btn = IconBtn("people", 30)
        self.acc_btn.setToolTip("Аккаунты")
        self.acc_btn.clicked.connect(self.app.open_accounts_menu)
        out = QPushButton("Выйти")
        out.setMaximumHeight(26)
        out.setObjectName("logoutBtn")
        out.clicked.connect(self.app.logout)
        me_row.addWidget(self.me_avatar)
        me_row.addWidget(self.me_name, 1)
        me_row.addWidget(self.acc_btn)
        me_row.addWidget(out)
        v.addLayout(me_row)
        self.drawer = QFrame(self)
        self.drawer.setObjectName("drawer")
        self.drawer.setFixedWidth(280)
        self.drawer.setStyleSheet(f"#drawer {{ background: {rgba(CUR['panel'], 255)}; border-right: 1px solid {rgba(CUR['stroke'], 255)}; }}")
        dv = QVBoxLayout(self.drawer)
        dv.setContentsMargins(14, 14, 14, 14)
        dv.setSpacing(6)
        dh = QHBoxLayout()
        dt = QLabel("Меню")
        dt.setObjectName("peerName")
        dh.addWidget(dt)
        dh.addStretch(1)
        dx = QPushButton("×")
        dx.setObjectName("ghostBtn")
        dx.setFixedSize(28, 28)
        dx.setStyleSheet("padding:0px; font-size:15px; font-weight:700;")
        dx.clicked.connect(self.close_drawer)
        dh.addWidget(dx)
        dv.addLayout(dh)
        for icon, label, fn in (("👤", "Мой профиль", self.open_my_profile),
                                ("📔", "Контакты", self.open_contacts),
                                ("👥", "Новая группа", self.create_group),
                                ("⚙️", "Настройки", self.open_settings),
                                ("🔒", "Заблокировать", self.app.lock_now), ("📖", "Моя история", self.my_story_click)):
            b = QPushButton(f"{icon}  {label}")
            b.setCursor(Qt.PointingHandCursor)
            b.setStyleSheet(f"background: {rgba(CUR['hover'], 170)}; border-radius: 12px; padding: 10px 12px; text-align: left; font-size: 14px; font-weight: 600; border: none; color: {CUR['text']};")
            b.clicked.connect(lambda _, f=fn: (self.close_drawer(), f()))
            dv.addWidget(b)
        dv.addStretch(1)
        self.drawer_dim = QWidget(self)
        self.drawer_dim.setStyleSheet("background: rgba(0,0,0,90);")
        self.drawer_dim.hide()
        self.drawer_dim.mousePressEvent = lambda e: self.close_drawer()
        self.drawer.hide()
        self._drawer_open = False
        return side

    def _check_upd(self):
        _c = getattr(self, "chat", None) or getattr(getattr(self, "app", None), "chat", None) or getattr(getattr(self, "app", None), "net", None) or getattr(getattr(self, "w", None), "chat", None)
        if _c is not None:
            try:
                _c.send_pkt({"type": "check_update", "hash": OWN_HASH})
                _c.send_pkt({"type": "ping"})
                _upd_dbg("sent check_update OWN_HASH=" + str(OWN_HASH)[:8])
                _c.send_pkt({"type": "users"})
                _c.send_pkt({"type": "presence_query", "user": _c.peer}) if (getattr(_c, "peer", None) and not str(_c.peer).startswith("g") and _c.peer != "saved") else None
            except Exception as _e:
                _upd_dbg("check_update ERR " + repr(_e))
        else:
            _upd_dbg("check_update: НЕ НАШЁЛ chat-объект")
    def show_update(self, pkt):
        self._upd_pkt = pkt
        self.upd_banner.setVisible(True)

    def _decline_update(self):
        self._declined_hash = getattr(self, "_upd_pkt", {}).get("hash")
        self.upd_banner.setVisible(False)

    def _do_update(self):
        pkt = getattr(self, "_upd_pkt", None)
        if not pkt:
            return
        try:
            import base64, os, subprocess
            raw = base64.b64decode(pkt["data"])
            p = os.path.abspath(__file__)
            with open(p, "wb") as f:
                f.write(raw)
            if getattr(sys, "frozen", False):
                try:
                    _do_self_restart()
                except Exception:
                    pass
            else:
                subprocess.Popen([sys.executable, p], cwd=os.path.dirname(p))
            os._exit(0)
        except Exception as ex:
            print("update err:", ex)

    def build_upd_banner(self):
        w = QFrame()
        w.setObjectName("updBanner")
        w.setVisible(False)
        w.setStyleSheet("#updBanner{background:#6c5ce7;} #updBanner QLabel{color:white;font-weight:600;background:transparent;}")
        h = QHBoxLayout(w)
        h.setContentsMargins(16, 8, 8, 8)
        h.setSpacing(8)
        lb = QLabel("🚀 Доступно обновление Bebsi")
        h.addWidget(lb)
        b = QPushButton("Обновить")
        b.setObjectName("bubbleMine")
        b.clicked.connect(self._do_update)
        h.addWidget(b)
        return w

    def build_chat(self):
        pane = ChatPane()
        self.pane = pane
        v = QVBoxLayout(pane)
        v.setContentsMargins(0, 0, 0, 0)
        v.setSpacing(0)

        hdr = QFrame()
        hdr.setAttribute(Qt.WA_StyledBackground, True)
        hdr.setObjectName("chatHeader")
        hdr.setFixedHeight(64)
        h = QHBoxLayout(hdr)
        h.setContentsMargins(20, 0, 20, 0)
        h.setSpacing(12)
        self.peer_avatar = AvatarWidget("?", 40, show_dot=True, clickable=True)
        self.peer_avatar.setToolTip("Информация")
        self.peer_avatar.clicked.connect(self.open_peer_info)
        hv = QVBoxLayout()
        hv.setSpacing(1)
        self.peer_name = QLabel(APP_NAME)
        self.peer_name.setObjectName("peerName")
        self.status_lbl = QLabel(APP_NAME)
        self.status_lbl.setObjectName("statusLbl")
        self.dots = TypingDots()
        self.dots.hide()
        hv.addWidget(self.peer_name)
        sh = QHBoxLayout()
        sh.setSpacing(6)
        sh.addWidget(self.status_lbl)
        sh.addWidget(self.dots)
        sh.addStretch(1)
        hv.addLayout(sh)
        h.addWidget(self.peer_avatar)
        h.addLayout(hv)
        h.addStretch(1)
        self.ttl_btn = QPushButton("⏳")
        self.ttl_btn.setObjectName("toolBtn")
        self.ttl_btn.setFixedSize(32, 32)
        self.ttl_btn.setToolTip("Исчезающие сообщения")
        self.ttl_btn.hide()
        self.ttl_btn.clicked.connect(self.ttl_menu)
        self.call_btn = IconBtn("call", 32)
        self.call_btn.setToolTip("Голосовой звонок")
        self.call_btn.clicked.connect(lambda: self.start_call(False))
        h.addWidget(self.call_btn)
        self.vcall_btn = IconBtn("vcam", 32)
        self.vcall_btn.setToolTip("Видеозвонок")
        self.vcall_btn.clicked.connect(lambda: self.start_call(True))
        h.addWidget(self.vcall_btn)
        v.addWidget(hdr)
        self.pin_bar = QFrame()
        self.pin_bar.setObjectName("banner")
        self.pin_bar.hide()
        pl = QHBoxLayout(self.pin_bar)
        pl.setContentsMargins(12, 4, 6, 4)
        self.pin_lbl = QLabel("")
        self.pin_lbl.setObjectName("subtitle")
        self.pin_lbl.setCursor(Qt.PointingHandCursor)
        self.pin_lbl.mouseReleaseEvent = lambda e: self._jump_pin()
        px = QPushButton("×")
        px.setObjectName("ghostBtn")
        px.setFixedSize(22, 22)
        px.setStyleSheet("padding:0px;")
        px.clicked.connect(self._unpin_cur)
        pl.addWidget(QLabel("📌"))
        pl.addWidget(self.pin_lbl, 1)
        pl.addWidget(px)
        v.addWidget(self.pin_bar)

        self.stack = QStackedWidget()
        empty = QWidget()
        ev = QVBoxLayout(empty)
        ev.setAlignment(Qt.AlignCenter)
        ev.setSpacing(8)
        em = QLabel("💬")
        f = em.font()
        f.setPointSize(56)
        em.setFont(f)
        et = QLabel("Выберите чат слева,\nчтобы начать переписку")
        et.setObjectName("emptyLbl")
        et.setAlignment(Qt.AlignCenter)
        ev.addWidget(em, 0, Qt.AlignHCenter)
        ev.addWidget(et)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.msg_w = QWidget()
        self.msg_l = QVBoxLayout(self.msg_w)
        self.msg_l.setContentsMargins(22, 18, 16, 18)
        self.msg_l.setSpacing(8)
        self.msg_l.addStretch(1)
        self.scroll.setWidget(self.msg_w)
        self.scroll.verticalScrollBar().valueChanged.connect(lambda _: self._safe_down())

        self.stack.addWidget(empty)
        self.stack.addWidget(self.scroll)
        hdr.hide()
        self.stack.currentChanged.connect(lambda i: hdr.setVisible(i != 0))
        v.addWidget(self.stack, 1)

        iw = QWidget()
        self.iw = iw
        iv = QVBoxLayout(iw)
        iv.setContentsMargins(14, 6, 14, 14)
        iv.setSpacing(6)

        self.banner = QFrame()
        self.banner.setObjectName("banner")
        self.banner.hide()
        bl = QHBoxLayout(self.banner)
        bl.setContentsMargins(12, 6, 6, 6)
        self.banner_lbl = QLabel(APP_NAME)
        self.banner_lbl.setObjectName("subtitle")
        bx = QPushButton("×")
        bx.setObjectName("ghostBtn")
        bx.setFixedSize(24, 24)
        bx.setStyleSheet("padding:0px;")
        bx.clicked.connect(self.cancel_banner)
        bl.addWidget(self.banner_lbl, 1)
        bl.addWidget(bx)
        iv.addWidget(self.banner)
        self.find_ed = QLineEdit()
        self.find_ed.setPlaceholderText("Найти в чате… (Enter — далее)")
        self.find_ed.hide()
        self.find_ed.returnPressed.connect(self.find_next)
        self._find_idx = -1
        iv.addWidget(self.find_ed)

        ih = QHBoxLayout()
        ih.setSpacing(4)
        self.attach = IconBtn("attach")
        self.attach.setFixedSize(40, 40)
        self.attach.setToolTip("Фото / файл")
        self.attach.clicked.connect(self.attach_menu)
        self.mic_btn = IconBtn("mic")
        self.mic_btn.setFixedSize(40, 40)
        self.mic_btn.setToolTip("Голосовое")
        self.mic_btn.clicked.connect(self.mic_click)
        self.circle_btn = IconBtn("circle")
        self.circle_btn.setFixedSize(40, 40)
        self.circle_btn.setToolTip("Кружок")
        self.circle_btn.clicked.connect(self.circle_click)
        self.input = QLineEdit()
        self.input.setObjectName("msgInput")
        self.input.setPlaceholderText("Сообщение…")
        self.input.returnPressed.connect(self.send_message)
        self.input.textChanged.connect(self.on_typing)
        self.emoji_btn = IconBtn("emoji", 30)
        self.emoji_btn.setFixedSize(40, 40)
        self.emoji_btn.setToolTip("Смайлики")
        self.emoji_btn.clicked.connect(self.open_emoji)
        self.send_btn = IconBtn("send")
        self.send_btn.setObjectName("sendBtn")
        self.send_btn.setFixedSize(40, 40)
        self.send_btn.setToolTip("Отправить")
        self.send_btn.clicked.connect(self.send_message)
        self.send_btn.installEventFilter(self)
        self._send_hold = False
        self._hold_t = QTimer(self)
        self._hold_t.setSingleShot(True)
        self._hold_t.setInterval(450)
        self._hold_t.timeout.connect(self._hold_fire)
        self.send_btn.setContextMenuPolicy(Qt.CustomContextMenu)
        self.send_btn.customContextMenuRequested.connect(self.sched_menu)
        self.emoji_btn.setParent(self.input)
        self.input.installEventFilter(self)
        self.emo_popup = QListWidget(self.iw)
        self.emo_popup.setFixedHeight(110)
        self.emo_popup.setMaximumWidth(220)
        self.emo_popup.hide()
        self.emo_popup.itemClicked.connect(self._emo_pick)
        self.input.setTextMargins(0, 0, 36, 0)
        ih.addWidget(self.attach)
        ih.addWidget(self.input, 1)
        ih.addWidget(self.mic_btn)
        ih.addWidget(self.circle_btn)
        ih.addWidget(self.send_btn)
        iv.addLayout(ih)
        v.addWidget(iw)
        self.down_btn = QPushButton("↓")
        self.down_btn.setParent(self.pane)
        self.down_btn.setFixedSize(40, 40)
        self.down_btn.setStyleSheet("background:" + CUR["accent"] + ";border-radius:20px;color:#fff;font-size:16px;font-weight:800;padding:0px;")
        self.down_btn.hide()
        self.down_btn.clicked.connect(self._down_click)
        return pane

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._place_drawer()
        self._upd_down_btn()
        self._upd_down_btn()
    def _place_drawer(self):
        d = getattr(self, "drawer", None)
        if d is None:
            return
        w = d.width()
        if not getattr(self, "_drawer_open", False):
            d.move(-w, 0)
        d.resize(w, self.height())
        self.drawer_dim.resize(self.width(), self.height())
        self.drawer_dim.move(0, 0)
    def toggle_drawer(self):
        if getattr(self, "_drawer_open", False):
            self.close_drawer()
        else:
            self.open_drawer()
    def open_drawer(self):
        self._drawer_open = True
        self._place_drawer()
        self.drawer_dim.show()
        self.drawer_dim.raise_()
        self.drawer.show()
        self.drawer.raise_()
        a = QPropertyAnimation(self.drawer, b"pos")
        a.setDuration(220)
        a.setStartValue(QPoint(-self.drawer.width(), 0))
        a.setEndValue(QPoint(0, 0))
        a.setEasingCurve(QEasingCurve.OutCubic)
        self._drawer_anim = a
        a.start()
    def close_drawer(self):
        if not getattr(self, "_drawer_open", False):
            return
        self._drawer_open = False
        a = QPropertyAnimation(self.drawer, b"pos")
        a.setDuration(180)
        a.setStartValue(self.drawer.pos())
        a.setEndValue(QPoint(-self.drawer.width(), 0))
        a.setEasingCurve(QEasingCurve.InCubic)
        a.finished.connect(self.drawer.hide)
        a.finished.connect(self.drawer_dim.hide)
        self._drawer_anim = a
        a.start()
    def cancel_banner(self):
        self.reply_info = None
        self.edit_mid = None
        self.banner.hide()
        self.input.setText("")

    def device_lists(self):
        mics, cams = [], []
        seen = set()
        try:
            import sounddevice as sd
            for i, d in enumerate(sd.query_devices()):
                nm = d["name"]
                low = nm.lower()
                if d["max_input_channels"] > 0 and nm not in seen \
                        and "primary" not in low and "первичн" not in low:
                    seen.add(nm)
                    mics.append((i, nm))
        except Exception:
            pass
        try:
            import cv2
            for i in range(4):
                cap = cv2.VideoCapture(i)
                if cap.isOpened():
                    cams.append((i, f"Камера {i}"))
                    cap.release()
        except Exception:
            pass
        return mics, cams

    def apply_devices(self, mic=None, cam=None):
        global MIC_DEV, CAM_DEV
        if mic is not None:
            MIC_DEV = int(mic)
        if cam is not None:
            CAM_DEV = int(cam)
        save_settings()

    def make_poll(self):
        if not self.peer:
            self.show_warn("Сначала выбери чат 👈")
            return
        dlg = PollDialog(self)
        if dlg.exec() != QDialog.Accepted:
            return
        q, opts = dlg.result_data()
        if not q or len(opts) < 2:
            self.show_warn("Нужен вопрос и минимум 2 варианта")
            return
        poll = json.dumps({"question": q, "options": opts, "votes": {}}, ensure_ascii=False)
        self.send_to(self.peer, poll=poll, last="Опрос")

    def _vote_poll(self, b, i):
        p = getattr(b, "poll_data", None)
        if not p:
            return
        votes = p.setdefault("votes", {})
        for k in list(votes.keys()):
            if self.me in votes[k]:
                votes[k].remove(self.me)
        votes.setdefault(str(i), [])
        if self.me not in votes[str(i)]:
            votes[str(i)].append(self.me)
        b.set_poll_votes(votes)

    def on_poll_vote(self, mid, opt):
        if not (mid and mid > 0):
            print("!! mid невалиден — сервер не присвоил id")
            return
        self.send_pkt({"type": "poll_vote", "msg_id": mid, "opt": opt})
        bb = self.bubbles_by_id.get(mid)
        if bb is not None and getattr(bb, "poll_data", None):
            p = bb.poll_data
            votes = p.setdefault("votes", {})
            for k in list(votes.keys()):
                if self.me in votes[k]:
                    votes[k].remove(self.me)
            votes.setdefault(str(opt), [])
            if self.me not in votes[str(opt)]:
                votes[str(opt)].append(self.me)
            bb.set_poll_votes(votes)
        for key in self.cache:
            for m in self.cache[key]:
                if m.get("id") == mid and m.get("poll"):
                    try:
                        p = json.loads(m["poll"])
                        votes = p.setdefault("votes", {})
                        for k in list(votes.keys()):
                            if self.me in votes[k]:
                                votes[k].remove(self.me)
                        votes.setdefault(str(opt), [])
                        if self.me not in votes[str(opt)]:
                            votes[str(opt)].append(self.me)
                        p["votes"] = votes
                        m["poll"] = json.dumps(p, ensure_ascii=False)
                    except Exception:
                        pass

    def on_poll_update(self, mid, votes):
        b = self.bubbles_by_id.get(mid)
        if b is not None:
            b.set_poll_votes(votes)
        for key in self.cache:
            for m in self.cache[key]:
                if m.get("id") == mid and m.get("poll"):
                    try:
                        p = json.loads(m["poll"])
                        p["votes"] = votes
                        m["poll"] = json.dumps(p, ensure_ascii=False)
                    except Exception:
                        pass

    def burn(self, b, key):
        try:
            row = b.parent()
            if row is not None:
                self.msg_l.removeWidget(row)
                self._stop_anims(row)
                row.deleteLater()
        except Exception:
            pass
        if b.mid:
            self.cache[key] = [m for m in self.cache.get(key, []) if m.get("id") != b.mid]

    def start_call(self, video):
        if str(self.peer or "").startswith("c") and str(self.peer)[1:].isdigit():
            self.show_warn("В каналах звонки отключены 📢")
            return
        if not self.peer:
            return
        w = self.window()
        w.call = CallDialog(w, w._call_send, self.peer, self.peer_name.text(), video, incoming=False)
        w.call.show()
        print("CALL SEND offer ->", self.peer)
        w._call_send({"type": "call_offer", "to": self.peer, "video": video})

    def ttl_menu(self):
        if not self.peer:
            return
        m = QMenu(self)
        acts = [m.addAction("⏳ Выкл"), m.addAction("⏳ 5 сек"), m.addAction("⏳ 30 сек"), m.addAction("⏳ 60 сек")]
        vals = [0, 5, 30, 60]
        act = m.exec(QCursor.pos())
        if act in acts:
            TTLS[self.peer] = vals[acts.index(act)]
            save_settings()
            self.update_ttl_btn()

    def update_ttl_btn(self):
        v = TTLS.get(self.peer or "", 0)
        self.ttl_btn.setText(f"⏳{v}" if v else "⏳")
        self.ttl_btn.setStyleSheet("background:#e67e22; border-radius:16px;" if v else "")

    def apply_theme(self, name):
        global CUR
        CUR = dict(THEMES.get(name, THEMES["Тёмная"]))
        QApplication.instance().setStyleSheet(build_qss(CUR))
        try:
            self.drawer.setStyleSheet(f"#drawer {{ background: {rgba(CUR['panel'], 255)}; border-right: 1px solid {rgba(CUR['stroke'], 255)}; }}")
            for b in self.drawer.findChildren(QPushButton):
                if b.objectName() in ("ghostBtn", "sendBtn"):
                    continue
                b.setStyleSheet(f"background: {rgba(CUR['hover'], 170)}; border-radius: 12px; padding: 10px 12px; text-align: left; font-size: 14px; font-weight: 600; border: none; color: {CUR['text']};")
            sep = self.findChild(QFrame, "sepLine")
            if sep is not None:
                sep.setStyleSheet(f"background:{rgba(CUR['stroke'], 255)}; max-height:1px; border:none;")
            self.down_btn.setStyleSheet("background:" + CUR["accent"] + ";border-radius:20px;color:#fff;font-size:16px;font-weight:800;padding:0px;")
        except Exception:
            pass
        self.pane.update()
        try:
            self.window().update()
        except Exception:
            pass
        save_settings()

    def apply_wallpaper(self, name):
        global WALL
        WALL = name
        self.pane.update()
        try:
            w = self.window()
            w.update()
            from PySide6.QtWidgets import QWidget
            for ch in w.findChildren(QWidget):
                ch.update()
        except Exception:
            pass
        save_settings()

    def open_settings(self):
        SettingsDialog(self, self).exec()

    def open_emoji(self):
        EmojiDialog(self, lambda e: self.input.insert(e)).exec()

    def send_pkt(self, obj):
        if self.app.net:
            self.app.net.send(obj)

    def ensure_chat(self, n):
        return self.chats.setdefault(n, {"online": False, "last": "", "ts": "", "unread": 0,
                                         "display": n, "bio": "", "avatar": "",
                                         "is_group": False, "members": [], "owner": ""})

    def set_me(self, name, profile):
        self.me = name
        self.my_profile = {"display": profile.get("display") or name,
                           "bio": profile.get("bio") or "", "avatar": profile.get("avatar") or ""}
        self.apply_my_profile()
        self.me_avatar.set_online(True)
        c = self.ensure_chat("saved")
        c["display"] = "🔖 Избранное"
        c["online"] = True
        it = ChatItem("saved")
        it.clicked.connect(self.open_chat)
        self.items["saved"] = it
        _sn = (SAVED or {}).get(name) or []
        if _sn:
            try:
                _l = _sn[-1].get("text") or ("📷 Фото" if _sn[-1].get("media") else ("🎤 Голосовое" if _sn[-1].get("voice") else ("⭕ Кружок" if _sn[-1].get("video") else ("📄 Файл" if _sn[-1].get("file_data") else ""))))
                it.set_last(_l, _sn[-1].get("ts") or "", "", "✓✓" if _sn[-1].get("mine") else "")
            except Exception:
                pass
        it.set_display("🔖 Избранное")
        it.avatar.set_name(name)

    def apply_my_profile(self):
        self.me_name.setText(self.my_profile["display"] or self.me)
        self.me_avatar.set_name(self.my_profile["display"] or self.me)
        self.me_avatar.set_avatar_b64(self.my_profile["avatar"])
        self.rebuild_stories()
        if self.peer == "saved":
            self.peer_avatar.set_name(self.my_profile["display"] or self.me)
            self.peer_avatar.set_avatar_b64(self.my_profile["avatar"])
        self.refresh_order()

    # ---------- кэш ----------
    def cache_add(self, key, text, ts, mine, media="", voice="", vdur=0, video="",
                  transcript="", sender="", reply_name="", reply_text="", fwd="",
                  file_name="", file_data="", edited=False, poll=""):
        self.cache.setdefault(key, []).append({"text": text, "ts": ts, "mine": mine,
                                               "media": media, "voice": voice, "vdur": vdur,
                                               "video": video, "transcript": transcript,
                                               "sender": sender, "id": None, "reactions": None,
                                               "reply_name": reply_name, "reply_text": reply_text,
                                               "fwd": fwd, "file_name": file_name,
                                               "file_data": file_data, "edited": edited,
                                               "poll": poll, "read": False})
        self.cache[key] = self.cache[key][-400:]

    def _render_cached(self, key, m):
        sender_name = ""
        if not m["mine"] and key.startswith("g"):
            sender_name = self.chats.get(m["sender"], {}).get("display", m["sender"])
        b = self.add_bubble(m["text"], m["ts"], mine=m["mine"], media=m["media"],
                            voice=m["voice"], vdur=m["vdur"], video=m["video"],
                            transcript=m["transcript"], sender_name=sender_name,
                            reply_name=m.get("reply_name", ""), reply_text=m.get("reply_text", ""),
                            fwd=m.get("fwd", ""), file_name=m.get("file_name", ""),
                            file_data=m.get("file_data", ""), edited=m.get("edited", False),
                            poll=m.get("poll", ""), animate=False)
        if m.get("id"):
            self._set_bid(b, m["id"], m.get("reactions"))
        if m.get("mine") and m.get("read"):
            b.set_read()
        return b

    def open_bubble_menu(self, d):
        menu = QMenu(self)
        for e in REACTIONS:
            s = e.strip()
            if not s or s == "\ufe0f" or len(s) < 2 and ord(s[0]) < 0x2000:
                continue
            menu.addAction(e)
        menu.addSeparator()
        a_rep = menu.addAction("↩ Ответить")
        a_quote = menu.addAction("❝ Цитировать выделенное")
        a_quote.setEnabled(bool((d.get("sel") or "").strip()))
        a_pick = menu.addAction("😀 Выбрать реакцию…")
        a_sel = menu.addAction("✅ Выделить / снять")
        a_copy = menu.addAction("📋 Копировать текст")
        a_fwd = menu.addAction("⇄ Переслать")
        a_pin = menu.addAction("📌 Закрепить")
        a_edit = menu.addAction("✎ Изменить") if d["mine"] else None
        a_del = menu.addAction("🗑 Удалить") if d["mine"] else None
        act = menu.exec(QCursor.pos())
        if not act:
            return
        if act.text() in REACTIONS and d["mid"]:
            self.send_pkt({"type": "react", "msg_id": d["mid"], "emoji": act.text()})
        elif act == a_copy:
            _sel = (d.get("sel") or "").strip()
            QApplication.clipboard().setText(_sel or d["text"])
        elif act == a_rep:
            nm = d["name"] or (self.me if d["mine"] else
                 (self.chats.get(self.peer, {}).get("display") or self.peer))
            self.reply_info = {"name": nm, "text": d["text"]}
            self.banner_lbl.setText(f"↩ Ответ: {nm} — {d['text'][:40]}")
            self.banner.show()
            self.input.setFocus()
        elif act == a_quote:
            sel = (d.get("sel") or "").strip()
            nm = d["name"] or (self.me if d["mine"] else
                (self.chats.get(self.peer, {}).get("display") or self.peer))
            self.reply_info = {"name": nm, "text": sel}
            self.banner_lbl.setText(f"❝ Цитата: {nm} — {sel[:40]}")
            self.banner.show()
            self.input.setFocus()
        elif act == a_pick:
            self.open_reaction_picker(d["mid"] or 0)
        elif act == a_fwd:
            self.start_forward(d)
        elif act == a_pin:
         lst = PINS_MSG.setdefault(str(self.peer), [])
         if d["mid"] in lst:
          lst.remove(d["mid"])
         else:
          lst.append(d["mid"])
         save_extra()
         self._upd_pin_bar()
        elif a_edit is not None and act == a_edit:
            self.edit_mid = d["mid"]
            self.input.setText(d["text"])
            self.banner_lbl.setText("✎ Редактирование сообщения")
            self.banner.show()
            self.input.setFocus()
        elif a_del is not None and act == a_del:
            self.send_pkt({"type": "delete", "msg_id": d["mid"]})
            self.apply_deleted(d["mid"])
            if act == a_sel and d["mid"]:
                mid = d["mid"]
                if mid in SEL_MIDS:
                    SEL_MIDS.discard(mid)
                else:
                    SEL_MIDS.add(mid)
                b = self.bubbles_by_id.get(mid)
                if b is not None:
                    b.setProperty("sel", "true" if mid in SEL_MIDS else "false")
                    b.style().unpolish(b)
                    b.style().polish(b)
                if SEL_MIDS:
                    mm = QMenu(self)
                    a_f = mm.addAction(f"⇄ Переслать выделенные ({len(SEL_MIDS)})")
                    a_d = mm.addAction(f"🗑 Удалить выделенные ({len(SEL_MIDS)})")
                    a_c = mm.addAction("✖ Снять выделение")
                    act2 = mm.exec(QCursor.pos())
                    if act2 == a_f:
                        targets = [("saved", "🔖 Избранное")] + [(k, self.chats.get(k, {}).get("display", k)) for k in self.items if k != "saved"]
                        fd = ForwardDialog(self, targets)
                        if fd.exec() == QDialog.Accepted and fd.result_key:
                            for _k2, _ms in self.cache.items():
                                for m in _ms:
                                    if m.get("id") in SEL_MIDS:
                                        self.send_to(fd.result_key, text=m.get("text") or "", media=m.get("media") or "", fwd=(self.my_profile["display"] or self.me) + " переслал(а)", last="⇄ Пересланное")
                        SEL_MIDS.clear()
                    elif act2 == a_d:
                        for mid2 in list(SEL_MIDS):
                            self.send_pkt({"type": "delete", "msg_id": mid2})
                            self.apply_deleted(mid2)
                        SEL_MIDS.clear()
                    elif act2 == a_c:
                        for mid2 in list(SEL_MIDS):
                            SEL_MIDS.discard(mid2)
                            b2 = self.bubbles_by_id.get(mid2)
                            if b2 is not None:
                                b2.setProperty("sel", "false")
                                b2.style().unpolish(b2)
                                b2.style().polish(b2)

    def start_forward(self, d):
        targets = [("saved", "🔖 Избранное")]
        for k, it in self.items.items():
            if k != "saved":
                targets.append((k, self.chats.get(k, {}).get("display", k)))
        dlg = ForwardDialog(self, targets)
        if dlg.exec() != QDialog.Accepted:
            return
        key = dlg.result_key
        if not key:
            return
        me_disp = self.my_profile["display"] or self.me
        orig = "себя" if d["mine"] else (d.get("fwd") or d["name"])
        self.send_to(key, text=d["text"], media=d.get("media", ""),
                     fwd=f"{me_disp} переслал(а) от {orig}", last="⇄ Пересланное")

    def apply_deleted(self, mid):
        b = self.bubbles_by_id.pop(mid, None)
        if b is not None:
            row = b.parent()
            if row is not None:
                self.msg_l.removeWidget(row)
                self._stop_anims(row)
                row.deleteLater()
        for key in list(self.cache.keys()):
            self.cache[key] = [m for m in self.cache[key] if m.get("id") != mid]

    def on_edited(self, mid, text):
        b = self.bubbles_by_id.get(mid)
        if b is not None:
            b.set_text(text)
        for key in self.cache.keys():
            for m in self.cache[key]:
                if m.get("id") == mid:
                    m["text"] = text
                    m["edited"] = True
        try:
            ok = getattr(self, "open_key", None)
            if ok and self.cache.get(ok):
                self.clear_messages()
                for m in self.cache.get(ok, []):
                    self._render_cached(ok, m)
                self.scroll_to_bottom()
        except Exception:
            pass

    def on_deleted(self, mid):
        self.apply_deleted(mid)

    # ---------- голосовые ----------
    def mic_click(self):
        if self.recorder is not None:
            self.recorder.stop()
            return
        if not self.peer:
            self.show_warn("Сначала выбери чат 👈")
            return
        try:
            import sounddevice
        except Exception:
            self.show_warn("Нужно: pip install sounddevice")
            return
        self.recorder = VoiceRecorder()
        self.recorder.finished_rec.connect(self.on_voice_done)
        self.recorder.start()
        self.rec_sec = 0
        self.rec_timer.start()
        self.mic_btn.setStyleSheet("background:#e74c3c; border-radius:20px;")

    def tick_rec(self):
        self.rec_sec += 1
        self.mic_btn.setText(f"{self.rec_sec}")
        ring = "rgba(255,255,255,170)" if self.rec_sec % 2 else "rgba(255,255,255,40)"
        self.mic_btn.setStyleSheet(f"background:#e74c3c; border-radius:20px; "
                                   f"border:3px solid {ring}; font-weight:700;")

    def on_voice_done(self, wav, dur):
        self.recorder = None
        self.rec_timer.stop()
        self.mic_btn.setText("🎤")
        self.mic_btn.setStyleSheet("")
        if not self.peer or dur < 0.5:
            return
        tr = transcribe_wav(wav)
        if not tr:
            self.show_warn("Ошибка в распознавании речи 🎤")
        b64 = base64.b64encode(wav).decode()
        self.send_to(self.peer, voice=b64, vdur=dur, transcript=tr, last="🎤 Голосовое")

    # ---------- кружки ----------
    def circle_click(self):
        if not self.peer:
            self.show_warn("Сначала выбери чат 👈")
            return
        try:
            import cv2
        except Exception:
            self.show_warn("Нужно: pip install opencv-python")
            return
        self.circle_rec = CircleRecorder()
        self.circle_rec.finished_rec.connect(self.on_circle_done)
        self.circle_dlg = QDialog(self)
        self.circle_dlg.setWindowTitle("Кружок")
        self.circle_dlg.setFixedSize(240, 100)
        cvl = QVBoxLayout(self.circle_dlg)
        self.circle_lbl = QLabel("⭕ Запись кружка… 8")
        self.circle_lbl.setObjectName("peerName")
        self.circle_lbl.setAlignment(Qt.AlignCenter)
        cvl.addWidget(self.circle_lbl)
        self.circle_left = 8
        ct = QTimer(self.circle_dlg)
        ct.setInterval(1000)

        def tick():
            self.circle_left -= 1
            self.circle_lbl.setText(f"⭕ Запись кружка… {max(self.circle_left, 0)}")
        ct.timeout.connect(tick)
        ct.start()
        self.circle_rec.start()
        self.circle_dlg.exec()

    def on_circle_done(self, mp4, wav, dur):
        if not mp4:
            if self.circle_dlg is not None:
                self.circle_dlg.close()
                self.circle_dlg = None
            self.show_warn("Камера не обнаружена 🎥")
            return
        if self.circle_dlg is not None:
            self.circle_dlg.accept()
            self.circle_dlg = None
        self.circle_rec = None
        if not self.peer or not mp4:
            self.show_warn("Камера не найдена 📷")
            return
        tr = transcribe_wav(wav) if wav else ""
        if wav and not tr:
            self.show_warn("Ошибка в распознавании речи 🎤")
        v64 = base64.b64encode(mp4).decode()
        self.send_to(self.peer, video=v64, transcript=tr, last="⭕ Кружок")

    # ---------- вложения ----------
    def eventFilter(self, o, e):
        try:
            if o is self.input and e.type() == QEvent.Resize:
                b = getattr(self, "emoji_btn", None)
                if b is not None:
                    h = self.input.height()
                    s = h - 10
                    b.resize(s, s)
                    b.move(self.input.width() - s - 5, 5)
            if o is getattr(self, "send_btn", None):
                if e.type() == QEvent.MouseButtonPress:
                    self._hold_t.start()
                elif e.type() == QEvent.MouseButtonRelease:
                    self._hold_t.stop()
                    if self._send_hold:
                        self._send_hold = False
                        return True
            return super().eventFilter(o, e)
        except Exception:
            return super().eventFilter(o, e)

    def reset_all(self):
        self.peer = None
        for w in list(self.items.values()):
            try:
                w.hide()
                w.deleteLater()
            except Exception:
                pass
        self.items.clear()
        self.chats.clear()
        self.cache.clear()
        self.my_bubbles.clear()
        self.bubbles_by_id.clear()
        self.clear_messages()
        self.stack.setCurrentIndex(0)
        self._set_input_vis(False)
        self.peer_name.setText("")
        self.status_lbl.setText("")

    def update_preview(self, key, msgs):
        _upd_dbg("PREVIEW " + str(key) + " n=" + str(len(msgs or [])))
        try:
            it = self.items.get(key)
            if it is None or not msgs:
                return
            m = msgs[-1]
            last = (m.get("text") or ("Опрос" if m.get("poll") else
                    "Голосовое" if m.get("voice") else
                    "Фото" if m.get("media") else
                    "Файл" if m.get("file_data") else "Сообщение"))
            if m.get("mine"):
                last = "Вы: " + last
            prefix = ""
            ticks = ("✓✓" if m.get("read", True) else "✓") if m.get("mine") else ""
            if not m.get("mine") and str(key).startswith("g") and str(key)[1:].isdigit():
                who = m.get("from") or m.get("frm") or ""
                dn = ""
                try:
                    dn = (self.all_names.get(who) or {}).get("display") or ""
                except Exception:
                    dn = ""
                prefix = (str(dn or who) + ": ") if who else ""
            f = getattr(it, "set_last", None) or getattr(it, "update_last", None)
            if f:
                f(last, m.get("ts") or "", prefix, ticks)
            else:
                lb = getattr(it, "last_lbl", None)
                if lb is not None:
                    lb.setText(last)
        except Exception as _e:
            _upd_dbg("PREVIEW ERR " + repr(_e))

    def burn_msg(self, key, ts):
        try:
            cache = self.cache.get(key, [])
            self.cache[key] = [m for m in cache if m.get("ts") != ts]
            it = self.items.get(key)
            if it is not None:
                if self.cache[key]:
                    self.update_preview(key, self.cache[key])
                else:
                    f = getattr(it, "set_last", None)
                    if f:
                        f("Нет сообщений")
        except Exception:
            pass

    def attach_menu(self):
        m = QMenu(self)
        a1 = m.addAction("📷 Фото")
        a2 = m.addAction("📁 Файл")
        a3 = m.addAction("✅ Опрос")
        act = m.exec(QCursor.pos())
        if act == a1:
            self.pick_media()
        elif act == a2:
            self.pick_file()
        elif act == a3:
            self.make_poll()

    def pick_media(self):
        if not self.peer:
            self.show_warn("Сначала выбери чат 👈")
            return
        path, _ = QFileDialog.getOpenFileName(self, "Отправить фото", "",
                                              "Изображения (*.png *.jpg *.jpeg *.webp *.bmp)")
        if not path:
            return
        b64 = image_to_b64(path, 1200, 82)
        if not b64:
            return
        print("MEDIA: b64 ок, len=", len(b64))
        dlg = PreviewDialog(self, b64)
        if dlg.exec() != QDialog.Accepted:
            return
        self.send_to(self.peer, text=dlg.caption(), media=b64, last="📷 Фото")

    def pick_file(self):
        if not self.peer:
            self.show_warn("Сначала выбери чат 👈")
            return
        path, _ = QFileDialog.getOpenFileName(self, "Отправить файл")
        if not path:
            return
        size = os.path.getsize(path)
        if size > 6_000_000:
            self.show_warn("Файл больше 6 МБ 😅")
            return
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        self.send_to(self.peer, file_name=os.path.basename(path), file_data=b64, last="📄 Файл")

    def save_file(self, name, data):
        if not data:
            return
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", name)
        if path:
            with open(path, "wb") as f:
                f.write(base64.b64decode(_(data)))

    def open_file(self, name, data):
        if not data:
            return
        try:
            import tempfile
            fn = os.path.basename(name or "file.bin") or "file.bin"
            path = os.path.join(tempfile.gettempdir(), "bebsi_" + fn)
            with open(path, "wb") as f:
                f.write(base64.b64decode(_(data)))
            os.startfile(path)
        except Exception as ex:
            print("OPEN FILE ERR:", ex)
            self.save_file(name, data)

    # ---------- отправка ----------
    def set_conn_status(self, ok):
        if not self.peer:
            return
        if ok:
            self.update_status()
        else:
            self.status_lbl.setText("нет соединения…")
            self.status_lbl.setStyleSheet("color:#e74c3c; font-size:12px;")

    def show_warn(self, text):
        self.status_lbl.show()
        self.status_lbl.setText(text)
        self.status_lbl.setStyleSheet("color:#f39c12; font-size:12px;")
        self.warn_timer.start(4000)

    def _clear_warn(self):
        if self.peer:
            self.update_status()
        else:
            self.status_lbl.setText("")

    def maybe_confetti(self, text):
        low = (text or "").lower()
        if is_big_emoji(text) or any(w in low for w in ("спасибо", "ура", "поздравля", "класс", "круто", "🎉")):
            Confetti(self.pane)

    def send_to(self, key, text="", media="", voice="", vdur=0, video="", transcript="",
                reply=None, fwd="", file_name="", file_data="", last="", poll=""):
        ts = datetime.now().isoformat(timespec="seconds")
        self.send_btn.setStyleSheet("background:#2ecc71;")
        QTimer.singleShot(250, lambda: self.send_btn.setStyleSheet(""))
        rn = reply["name"] if reply else ""
        rt = reply["text"] if reply else ""
        self.cache_add(key, text, ts, True, media, voice, vdur, video, transcript,
                       reply_name=rn, reply_text=rt, fwd=fwd, file_name=file_name,
                       file_data=file_data, poll=poll)
        self.maybe_confetti(text)
        if key == self.peer:
            self.add_bubble(text, ts, mine=True, media=media, voice=voice, vdur=vdur,
                            video=video, transcript=transcript, reply_name=rn,
                            reply_text=rt, fwd=fwd, file_name=file_name, file_data=file_data,
                            poll=poll)
        to = self.me if key == "saved" else key
        if key.startswith("c") and key[1:].isdigit():
            self.send_pkt({"type": "channel_post", "channel": int(key[1:]), "text": text, "media": media, "voice": voice, "vdur": vdur, "video": video, "transcript": transcript, "fwd": fwd, "reply_name": rn, "reply_text": rt, "file_name": file_name, "file_data": file_data, "poll": poll})
        elif key.startswith("g"):
            self.send_pkt({"type": "group_message", "ttl": TTLS.get(key, 0), "group": int(key[1:]), "text": text, "media": media, "voice": voice, "vdur": vdur, "video": video, "transcript": transcript, "fwd": fwd, "reply_name": rn, "reply_text": rt, "file_name": file_name, "file_data": file_data, "poll": poll})
        else:
            self.send_pkt({"type": "message", "ttl": TTLS.get(key, 0), "to": to, "text": text, "media": media, "voice": voice, "vdur": vdur, "video": video, "transcript": transcript, "fwd": fwd, "reply_name": rn, "reply_text": rt, "file_name": file_name, "file_data": file_data, "poll": poll})
            if key == "saved":
                SAVED.setdefault(self.me, []).append({"text": text, "ts": ts, "mine": True, "media": media, "voice": voice, "vdur": vdur, "video": video, "transcript": transcript, "file_name": file_name, "file_data": file_data})
                SAVED[self.me] = SAVED[self.me][-500:]
                save_settings()
        c = self.ensure_chat(key)
        c["last"], c["ts"] = last or text or "📷 Фото", ts
        if key in self.items:
            pre = "" if (key.startswith("g") or key == "saved") else "Вы: "
            self.items[key].set_last(pre + c["last"], ts, "", "✓")
        self.refresh_order()

    def _hold_fire(self):
        self._send_hold = True
        self.sched_menu()
    def sched_menu(self, pos=None):
        from datetime import timedelta
        text = self.input.text().strip()
        if not text or not self.peer:
            self.show_warn("Сначала напиши сообщение ✍")
            return
        m = QMenu(self)
        a_now = m.addAction("⚡ Отправить сейчас")
        a1 = m.addAction("⏰ Через час")
        a2 = m.addAction("🌅 Завтра в 9:00")
        a3 = m.addAction("🕐 Выбрать время…")
        act = m.exec(QCursor.pos())
        if act == a_now:
            self.send_message()
        elif act == a1:
            self._schedule_send(datetime.now() + timedelta(hours=1))
        elif act == a2:
            nt = datetime.now() + timedelta(days=1)
            self._schedule_send(nt.replace(hour=9, minute=0, second=0, microsecond=0))
        elif act == a3:
            from PySide6.QtWidgets import QTimeEdit
            d = QDialog(self)
            d.setWindowTitle("Когда отправить")
            v = QVBoxLayout(d)
            v.setContentsMargins(20, 20, 20, 20)
            v.setSpacing(10)
            lb = QLabel("Время отправки (если прошло — завтра):")
            lb.setObjectName("subtitle")
            v.addWidget(lb)
            te = QTimeEdit()
            te.setDisplayFormat("HH:mm")
            v.addWidget(te)
            okb = QPushButton("Запланировать")
            okb.setObjectName("sendBtn")
            okb.clicked.connect(d.accept)
            v.addWidget(okb)
            if d.exec() == QDialog.Accepted:
                q = te.time()
                dt = datetime.now().replace(hour=q.hour(), minute=q.minute(), second=0, microsecond=0)
                if dt <= datetime.now():
                    dt += timedelta(days=1)
                self._schedule_send(dt)
    def _schedule_send(self, dt):
        text = self.input.text().strip()
        if not text or not self.peer:
            return
        SCHED.setdefault(self.me, []).append({"key": self.peer, "text": text, "ts": dt.isoformat(timespec="seconds")})
        save_extra()
        self.input.clear()
        self.show_warn("Запланировано на " + dt.strftime("%d.%m %H:%M") + " ⏰")
    def _sched_tick(self):
        jobs = SCHED.get(self.me) or []
        if not jobs:
            return
        now = datetime.now()
        rest = []
        fired = 0
        for j in jobs:
            try:
                t = datetime.fromisoformat(j["ts"])
            except Exception:
                continue
            if t <= now:
                self.send_to(j["key"], text=j["text"], last=j["text"])
                fired += 1
            else:
                rest.append(j)
        if fired:
            SCHED[self.me] = rest
            save_extra()
            self.show_warn("⏰ Отложенное отправлено")

    def send_message(self):
        if self.peer in BLOCKED:
            self.show_warn("Собеседник заблокирован 🚫")
            return
        text = self.input.text().strip()
        if self.edit_mid:
            if text:
                self.send_pkt({"type": "edit", "msg_id": self.edit_mid, "text": text})
                self.on_edited(self.edit_mid, text)
                b = self.bubbles_by_id.get(self.edit_mid)
                if b is not None:
                    b.set_text(text)
                for m in self.cache.get(self.peer, []):
                    if m.get("id") == self.edit_mid:
                        m["text"] = text
                        m["edited"] = True
            self.cancel_banner()
            return
        if not text or not self.peer:
            return
        self.input.clear()
        rep = self.reply_info
        self.reply_info = None
        self.banner.hide()
        self.send_to(self.peer, text=text, reply=rep, last=text)
        DRAFTS[self.peer] = ""
        save_extra()

    # ---------- профили и группы ----------
    def open_my_profile(self):
        dlg = ProfileDialog(self, own=True, username=self.me,
                            display=self.my_profile["display"], bio=self.my_profile["bio"],
                            avatar=self.my_profile["avatar"])
        if dlg.exec() == QDialog.Accepted:
            data = dlg.result_data()
            if not data["display"]:
                data["display"] = self.me
            self.my_profile.update(data)
            self.apply_my_profile()
            self.send_pkt({"type": "profile", **data})

    def open_peer_info(self):
        if not self.peer:
            return
        try:
            PeerInfoDialog(self, self.peer).exec()
        except Exception as _e:
            print("PEER INFO ERR:", _e)
            self.show_warn("Профиль не открылся — причина в консоли")
    def handle_profile(self, user, display, bio, avatar):
        if user == self.me:
            return
        if user not in self.chats:
            return
        c = self.chats[user]
        c["display"], c["bio"], c["avatar"] = display, bio, avatar
        if user in self.items:
            self.items[user].set_display(display or user)
            self.items[user].avatar.set_avatar_b64(avatar)
        if user == self.peer:
            self.peer_name.setText(CONTACT_NAMES.get(user) or display or user)
            self.peer_avatar.set_avatar_b64(avatar)
        self.rebuild_stories()

    def create_channel(self):
        name, ok = QInputDialog.getText(self, "Новый канал", "Название канала:")
        if not ok or not name.strip():
            return
        desc, _ = QInputDialog.getText(self, "Новый канал", "Описание (необязательно):")
        self.send_pkt({"type": "channel_create", "name": name.strip()[:40], "desc": (desc or "").strip()[:120]})
        self.show_warn("Канал создаётся… 📢")
    def find_channel(self):
        q, ok = QInputDialog.getText(self, "Найти канал", "Запрос:")
        if not ok or not q.strip():
            return
        self.send_pkt({"type": "channel_search", "q": q.strip().lower()})
    

    def open_channel_settings(self):
        key = getattr(self, "peer", None) or ""
        if not (str(key).startswith("c") and str(key)[1:].isdigit()):
            self.show_warn("Открой канал, чтобы управлять им ⚙")
            return
        ChannelSettingsDialog(self, key).exec()

    def replay_guide(self):
        try:
            self.close_drawer()
        except Exception:
            pass
        QTimer.singleShot(250, lambda: _start_guide(self))
    def create_group(self):
        users = [(n, self.chats[n]["display"]) for n in self.chats
                 if not self.chats[n]["is_group"] and n != "saved"]
        dlg = GroupDialog(self, users)
        if dlg.exec() != QDialog.Accepted:
            return
        name, members = dlg.result_data()
        if not name:
            return
        self.send_pkt({"type": "group_create", "name": name, "members": members})

    def handle_channels(self, chs):
        for ch in chs:
            key = "c" + str(ch["id"])
            c = self.ensure_chat(key)
            c["display"] = "📢 " + (ch.get("name") or key)
            c["is_group"] = True
            c["is_channel"] = True
            c["owner"] = ch.get("owner") or ""
            c["members"] = ch.get("subs") or []
            c["online"] = True
            if key not in self.items:
                it = ChatItem(key, is_group=True)
                it.ctx.connect(self.open_chat_menu)
                it.clicked.connect(self.open_chat)
                self.items[key] = it
                fade_in(it, 300)
            self.items[key].set_display(c["display"])
        self.refresh_order()
    def incoming_channel_message(self, cid, frm, text, ts, mid=None, reactions=None, **e):
        key = "c" + str(cid)
        mine = frm == self.me
        c = self.ensure_chat(key)
        if key not in self.items:
            it = ChatItem(key, is_group=True)
            it.ctx.connect(self.open_chat_menu)
            it.clicked.connect(self.open_chat)
            self.items[key] = it
        c["last"], c["ts"] = text or ("📷 Фото" if e.get("media") else ("📄 Файл" if e.get("file_data") else "📢 Пост")), ts
        self.cache_add(key, text, ts, mine, sender=frm, **e)
        if key == self.peer:
            c["unread"] = 0
            if key in self.items:
                self.items[key].set_unread(0)
            b = self.add_bubble(text, ts, mine=mine, sender_name=("" if mine else (c.get("display") or frm)), **e)
            if mid:
                self._set_bid(b, mid, reactions)
        else:
            c["unread"] += 1
            if key in self.items:
                self.items[key].set_unread(c["unread"])
        if key in self.items:
            self.items[key].set_last(c["last"], ts)
        self.refresh_order()
    def handle_channel_history(self, cid, messages):
        self.handle_history("c" + str(cid), messages)
    
    def handle_groups(self, groups):
        for g in groups:
            key = f"g{g['id']}"
            c = self.ensure_chat(key)
            c["display"] = g["name"]
            c["is_group"] = True
            c["online"] = True
            c["members"] = g["members"]
            c["owner"] = g["owner"]
            if key not in self.items:
                it = ChatItem(key, is_group=True)
                it.clicked.connect(self.open_chat)
                self.items[key] = it
                fade_in(it, 300)
            self.items[key].set_display("👥 " + g["name"])
        self.refresh_order()

    # ---------- истории ----------
    def _story_widget(self, name, disp, is_me):
        w = QWidget()
        vv = QVBoxLayout(w)
        vv.setSpacing(2)
        vv.setContentsMargins(0, 0, 0, 0)
        av = AvatarWidget(name, 54, clickable=True, ring=True)
        if is_me:
            av.set_avatar_b64(self.my_profile.get("avatar", ""))
            av.setToolTip("Моя история")
            av.clicked.connect(self.my_story_click)
        else:
            av.set_avatar_b64(self.chats.get(name, {}).get("avatar", ""))
            av.setToolTip(disp)
            av.clicked.connect(lambda u=name: self.view_stories(u))
        lb = QLabel((disp or name)[:9])
        lb.setObjectName("itemTime")
        lb.setAlignment(Qt.AlignCenter)
        vv.addWidget(av, 0, Qt.AlignHCenter)
        vv.addWidget(lb)
        return w

    def rebuild_stories(self):
        while self.story_l.count() > 1:
            item = self.story_l.takeAt(0)
            if item.widget():
                self._stop_anims(item.widget())
                item.widget().deleteLater()
        self.story_l.insertWidget(0, self._story_widget(self.me or "?",
                                                        self.my_profile.get("display") or self.me or "Я",
                                                        True))
        i = 1
        for user, stories in self.story_data.items():
            if user == self.me or not stories:
                continue
            self.story_l.insertWidget(i, self._story_widget(
                user, self.chats.get(user, {}).get("display", user), False))
            i += 1
        has = any(len(v) for v in self.story_data.values())
        self.story_scroll.setVisible(bool(has))

    def handle_stories(self, stories):
        self.story_data = {}
        for s in stories:
            self.story_data.setdefault(s["user"], []).append(s)
        self.rebuild_stories()

    def on_story_new(self, sid, user, media, caption, ts):
        self.story_data.setdefault(user, []).append(
            {"id": sid, "user": user, "media": media, "caption": caption, "ts": ts})
        self.rebuild_stories()

    def my_story_click(self):
        if self.story_data.get(self.me):
            self.view_stories(self.me)
        else:
            self.add_story()

    def add_story(self):
        path, _ = QFileDialog.getOpenFileName(self, "Новая история", "",
                                              "Изображения (*.png *.jpg *.jpeg *.webp *.bmp)")
        if not path:
            return
        b64 = image_to_b64(path, 900, 80)
        if not b64:
            return
        caption, _ = QInputDialog.getText(self, "История", "Подпись (необязательно):")
        self.send_pkt({"type": "story_add", "media": b64, "caption": caption})

    def view_stories(self, start_user):
        flat = []
        order = [start_user] + [u for u in self.story_data if u != start_user]
        for u in order:
            for s in self.story_data.get(u, []):
                disp = u if u == self.me else self.chats.get(u, {}).get("display", u)
                flat.append((u, disp, s))
        if not flat:
            return
        idx = next((i for i, x in enumerate(flat) if x[0] == start_user), 0)
        StoryViewer(self, flat, idx).exec()

    # ---------- события сервера ----------
    def handle_users(self, users, chats=None):
        self.all_names = {u["name"]: u for u in users}
        new_i = 0
        for u in users:
            n = u["name"]
            if n == self.me:
                continue
            if chats is not None and n not in chats and n not in self.chats:
                continue
            c = self.ensure_chat(n)
            c["online"] = u["online"]
            c["display"] = u.get("display") or n
            c["bio"] = u.get("bio") or ""
            c["avatar"] = u.get("avatar") or ""
            if n not in self.items:
                it = ChatItem(n)
                it.ctx.connect(self.open_chat_menu)
                if n in CONTACT_NAMES and n not in BLOCKED:
                    it.set_display(CONTACT_NAMES[n])
                if n in DELETED:
                    it.hide()
                if n in BLOCKED:
                    it.set_display("🚫 " + n)
                it.clicked.connect(self.open_chat)
                self.items[n] = it
                fade_in(it, 300, delay=new_i * 70)
                new_i += 1
            self.items[n].set_online(c["online"])
            self.items[n].set_display(c["display"])
            self.items[n].avatar.set_avatar_b64(c["avatar"])
        self.refresh_order()

        for key in list(self.cache):
            self.update_preview(key, self.cache[key])
        if self.peer:
            self.update_status()

    def handle_presence(self, user, online):
        if user == self.me:
            return
        if user not in self.chats:
            return
        c = self.chats[user]
        c["online"] = online
        if online:
            self.last_seen.pop(user, None)
        else:
            self.last_seen[user] = datetime.now().strftime("%H:%M")
        if online and user not in self.items:
            it = ChatItem(user)
            it.clicked.connect(self.open_chat)
            self.items[user] = it
        if user in self.items:
            self.items[user].set_online(online)
        if user == self.peer:
            self.peer_avatar.set_online(online)
            self.update_status()
        self.refresh_order()
    def _bind_bubble(self, b):
        b.react.connect(self.send_react)
        b.picker.connect(self.open_reaction_picker)
        b.view.connect(lambda m: ImageViewer(self, m).exec())
        b.view_video.connect(lambda v, tr: VideoDialog(self, v, tr).exec())
        b.file_save.connect(self.open_file)
        b.ctx.connect(self.open_bubble_menu)
        b.poll_vote_sig.connect(self.on_poll_vote)
        if getattr(b, "poll_w", None) is not None:
            b.poll_w.vote.connect(lambda i, bb=b: self._vote_poll(bb, i))

    def _extra(self, pkt):
        return {"media": pkt.get("media", ""), "voice": pkt.get("voice", ""),
                "vdur": pkt.get("vdur", 0), "video": pkt.get("video", ""),
                "transcript": pkt.get("transcript", ""), "reply_name": pkt.get("reply_name", ""),
                "reply_text": pkt.get("reply_text", ""), "fwd": pkt.get("fwd", ""),
                "file_name": pkt.get("file_name", ""), "file_data": pkt.get("file_data", ""), "poll": pkt.get("poll", "")}

    def incoming_message(self, frm, text, ts, mid=None, reactions=None, force_key=None, **e):
        mine = frm == self.me
        key = force_key or ("saved" if mine else frm)
        if key in DELETED:
            DELETED.discard(key)
            save_extra()
        # DEDUP1
        if any(m.get("ts") == ts and m.get("text") == text and bool(m.get("mine")) == bool(mine)
            for m in (self.cache.get(key) or [])[-6:]):
            return
        c = self.ensure_chat(key)
        if key not in self.items:
            it = ChatItem(key)
            it.clicked.connect(self.open_chat)
            self.items[key] = it
        c["last"], c["ts"] = text or ("🎤 Голосовое" if e.get("voice") else "⭕ Кружок" if e.get("video") else "📄 Файл" if e.get("file_data") else "📷 Фото"), ts
        self.cache_add(key, text, ts, mine, sender=frm, **e)
        self.maybe_confetti(text)
        if key == self.peer:
            c["unread"] = 0
            if key in self.items:
                self.items[key].set_unread(0)
            b = self.add_bubble(text, ts, mine=mine, **e)
            if mid:
                self._set_bid(b, mid, reactions)
            if not mine:
                self.send_pkt({"type": "read", "to": frm})
        else:
            c["unread"] += 1
            if key in self.items:
                self.items[key].set_unread(c["unread"])
        if key in self.items:
            self.items[key].set_last(c["last"], ts)
        self.refresh_order()

    def incoming_group_message(self, gid, frm, text, ts, mid=None, reactions=None, **e):
        key = f"g{gid}"
        mine = frm == self.me
        if key in DELETED:
            DELETED.discard(key)
            save_extra()
        c = self.ensure_chat(key)
        if key not in self.items:
            it = ChatItem(key, True)
            it.clicked.connect(self.open_chat)
            self.items[key] = it
        c["is_group"], c["online"] = True, True
        c["last"], c["ts"] = text or ("🎤 Голосовое" if e.get("voice") else "⭕ Кружок" if e.get("video") else "📄 Файл" if e.get("file_data") else "📷 Фото"), ts
        sender_disp = self.chats.get(frm, {}).get("display", frm)
        self.cache_add(key, text, ts, mine, sender=frm, **e)
        if key == self.peer:
            c["unread"] = 0
            if key in self.items:
                self.items[key].set_unread(0)
            b = self.add_bubble(text, ts, mine=mine, sender_name=("" if mine else sender_disp), **e)
            if mid:
                self._set_bid(b, mid, reactions)
        else:
            c["unread"] += 1
            if key in self.items:
                self.items[key].set_unread(c["unread"])
        if key in self.items:
            self.items[key].set_last(f"{sender_disp}: {c['last']}", ts)
        self.refresh_order()

    def handle_history(self, peer, messages):
        try:
            if peer == "saved" and not messages:
                msgs = []
                for _m in SAVED.get(getattr(self, "me", None) or "", []):
                    d = {"media": "", "voice": "", "vdur": 0, "video": "", "transcript": "",
                         "id": None, "reactions": None, "reply_name": "", "reply_text": "",
                         "fwd": "", "file_name": "", "file_data": "", "edited": 0, "poll": ""}
                    d.update(_m)
                    d["from"] = self.me
                    d["ts"] = d.get("ts") or ""
                    msgs.append(d)
                messages = msgs
            if messages:
                _seen = set(); _uniq = []
                for _m in messages:
                    _k = (_m.get("ts"), _m.get("text"), _m.get("from"))
                    if _k in _seen: continue
                    _seen.add(_k); _uniq.append(_m)
                messages = _uniq
                _old_read = {}
                for _m in self.cache.get(peer, []):
                    if _m.get("mine"):
                        _old_read[(_m.get("ts"), _m.get("text"))] = bool(_m.get("read"))
                self.cache[peer] = [{"text": m["text"], "ts": m["ts"],
                                     "mine": m["from"] == self.me,
                                     "media": m.get("media", ""), "voice": m.get("voice", ""),
                                     "vdur": m.get("vdur", 0), "video": m.get("video", ""),
                                     "transcript": m.get("transcript", ""),
                                     "sender": m["from"], "id": m.get("id"),
                                     "reactions": m.get("reactions"),
                                     "reply_name": m.get("reply_name", ""),
                                     "reply_text": m.get("reply_text", ""),
                                     "fwd": m.get("fwd", ""), "file_name": m.get("file_name", ""),
                                     "file_data": m.get("file_data", ""),
                                     "edited": m.get("edited", 0), "poll": m.get("poll", "")} for m in messages]
                for _m in self.cache[peer]:
                    if _m.get("mine"):
                        _m["read"] = _old_read.get((_m.get("ts"), _m.get("text")), False)
                    else:
                        _m.setdefault("read", True)
                self.cache[peer] = sorted(self.cache[peer], key=lambda _x: _x.get("ts") or "")[-400:]
                self.update_preview(peer, self.cache[peer])
            if peer != self.peer:
                return
            self.clear_messages()
            for m in (self.cache.get(peer) or [])[-300:]:
                self._render_cached(peer, m)
            self.scroll_to_bottom(60)
        except Exception as _e:
            print("HISTORY ERR:", _e)
            try:
                with open(os.path.join(DIR, "saved_err.log"), "a", encoding="utf-8") as f:
                    f.write(repr(_e) + "\n")
            except Exception:
                pass
    def handle_group_history(self, gid, messages):
        _upd_dbg("HIST CALL line")
        self.handle_history(f"g{gid}", messages)

    def _set_bid(self, b, mid, reactions):
        b.mid = mid
        self.bubbles_by_id[mid] = b
        if reactions:
            b.set_reactions(reactions, self.me)

    def on_ack_id(self, mid):
        for b in reversed(self.my_bubbles.get(self.peer, [])):
            if b.mid is None:
                self._set_bid(b, mid, None)
                for m in reversed(self.cache.get(self.peer, [])):
                    if m["mine"] and not m.get("id"):
                        m["id"] = mid
                        break
                break

    def on_reaction(self, mid, reactions):
        b = self.bubbles_by_id.get(mid)
        if b:
            b.set_reactions(reactions, self.me)

    def send_react(self, mid, emoji):
        if mid and mid > 0:
            self.send_pkt({"type": "react", "msg_id": mid, "emoji": emoji})

    def open_reaction_picker(self, mid):
        menu = QMenu(self)
        for e in REACTIONS:
            s = e.strip()
            if not s or s == "\ufe0f" or len(s) < 2 and ord(s[0]) < 0x2000:
                continue
            menu.addAction(e)
        act = menu.exec()
        if act:
            self.send_pkt({"type": "react", "msg_id": mid, "emoji": act.text()})

    def on_read(self, frm):
        for b in self.my_bubbles.get(frm, []):
            b.set_read()
        ch = self.cache.get(frm)
        if ch:
            for m in ch:
                if m.get("mine"): m["read"] = True
            self.update_preview(frm, ch)

    def on_typing_event(self, frm):
        if frm != self.peer:
            return
        self.status_lbl.hide()
        self.dots.show()
        self.dots.start()
        self.typing_timer.stop()
        self.typing_timer.start(3000)

    def hide_typing(self):
        self.dots.stop()
        self.dots.hide()
        self.status_lbl.show()

    def close_chat(self):
        if self.peer:
            DRAFTS[self.peer] = self.input.text()
            save_extra()
        self.peer = None
        global CURRENT_PEER
        CURRENT_PEER = ""
        for n, it in self.items.items():
            it.set_selected(False)
        self.clear_messages()
        self.stack.setCurrentIndex(0)
        self._set_input_vis(False)
        self.peer_name.setText("")
        self.status_lbl.setText("")
        self.hide_typing()
        self.cancel_banner()

    def keyPressEvent(self, e):
        mod = e.modifiers() & Qt.ControlModifier
        if e.key() == Qt.Key_Escape:
            if getattr(self, "find_ed", None) is not None and self.find_ed.isVisible():
                self.find_ed.hide()
            elif self.peer:
                self.close_chat()
        elif mod and e.key() == Qt.Key_K:
            self.search.setFocus()
        elif mod and e.key() == Qt.Key_N:
            self.close_chat()
            self.search.setFocus()
        elif mod and e.key() == Qt.Key_F and self.peer:
            self.find_ed.setVisible(not self.find_ed.isVisible())
            if self.find_ed.isVisible():
                self.find_ed.setFocus()
        else:
            super().keyPressEvent(e)

    def slide_in(self, w):
        try:
            old = getattr(w, "_slide", None)
            if old is not None:
                try:
                    old.stop()
                except Exception:
                    pass
            w.setProperty("slide_pos", 0.0)
            a = QPropertyAnimation(w, b"slide_pos")
            a.setDuration(260)
            a.setStartValue(0.0)
            a.setEndValue(1.0)
            a.setEasingCurve(QEasingCurve.OutCubic)
            w._slide = a
            a.start()
        except Exception as e:
            print("SLIDE ERR:", e)
    def _set_input_vis(self, on):
        try:
            self.iw.setVisible(bool(on))
        except Exception:
            pass
    def _on_search(self, txt):
        try:
            QTimer.singleShot(350, lambda: self._do_search(txt))
        except Exception:
            pass
    
    def _do_search(self, txt):
        try:
            if self.search.text() != txt or len(txt.strip()) < 2:
                return
            self.app.net.send({"type": "search_users", "q": txt.strip()})
        except Exception:
            pass
    
    def open_chat(self, key):
        try:
            self._open_chat_impl(key)
        except Exception as _e:
            import traceback
            print("OPEN CHAT ERR:", _e)
            traceback.print_exc()
            try:
                with open(os.path.join(DIR, "open_chat_err.log"), "a", encoding="utf-8") as f:
                    f.write(traceback.format_exc() + "\n")
            except Exception:
                pass
            self.show_warn("Чат открылся с ошибкой — причина в open_chat_err.log")
    def _open_chat_impl(self, key):
        self.app.last_peer = key
        _upd_dbg("OPEN CHAT " + str(key))
        if self.peer and self.peer != key:
            DRAFTS[self.peer] = self.input.text()
            save_extra()
        self.peer = key
        global CURRENT_PEER
        CURRENT_PEER = key
        if key in DELETED:
            DELETED.discard(key)
            save_extra()
            _it = self.items.get(key)
            if _it:
                _it.show()
        self.input.setEnabled(self.peer not in BLOCKED)
        for n, it in self.items.items():
            it.set_selected(n == key)
        c = self.ensure_chat(key)
        _unreads_before = c.get("unread", 0)
        c["unread"] = 0
        if key in self.items:
            self.items[key].set_unread(0)
        is_group = key.startswith("g")
        is_chan = key.startswith("c") and key[1:].isdigit()
        is_saved = key == "saved"
        self.open_key = key
        disp = ("📌 Избранное" if is_saved else (CONTACT_NAMES.get(key) or c["display"]))
        self.peer_avatar.set_name(self.me if is_saved else c["display"])
        self.peer_avatar.set_avatar_b64(self.my_profile.get("avatar", "") if is_saved else ("" if is_group else c["avatar"]))
        self.peer_avatar.set_online(c["online"])
        self.peer_avatar.show_dot = not is_saved
        self.call_btn.setVisible(not is_chan)
        self.vcall_btn.setVisible(not is_chan)
        self.peer_avatar.update()
        self.peer_name.setText(disp)
        self.send_pkt({"type": "users"})
        self.update_status()
        if not is_group and not is_saved and not is_chan:
            self.send_pkt({"type": "presence_query", "user": key})
        self.update_ttl_btn()
        self.hide_typing()
        self.stack.setCurrentIndex(1)
        self._set_input_vis(True)
        if is_chan and c.get("owner") != self.me:
            self._set_input_vis(False)
        self._missed = 0
        self.clear_messages()
        self._missed = 0
        self._upd_down_btn()
        _slice = (self.cache.get(key) or [])[-300:]
        _cut = len(_slice) - _unreads_before if _unreads_before else -1
        for _i, m in enumerate(_slice):
         if _cut >= 0 and _i == _cut:
          self._insert_new_line()
         self._render_cached(key, m)
        if self.cache.get(key):
            self.scroll_to_bottom()
        try:
            try:
                try:
                    try:
                        try:  # SLIDEWRAP
                            self.slide_in(self.scroll)
                        except Exception:
                            pass
                    except Exception:
                        pass
                except Exception as _se:
                    print("SLIDE ERR:", _se)
            except Exception as _se:
                print("SLIDE ERR:", _se)
        except Exception as _e:
            print("SLIDE ERR:", _e)
        self._upd_down_btn()
        self._upd_pin_bar()
        if is_chan:
            self.send_pkt({"type": "channel_history", "channel": int(key[1:])})
        elif is_group:
            self.send_pkt({"type": "group_history", "group": int(key[1:])})
        else:
            self.send_pkt({"type": "history", "peer": self.me if is_saved else key})
            if not is_saved:
                self.send_pkt({"type": "read", "to": key})
        QTimer.singleShot(3000, lambda k=key: self._hist_retry(k))
        self.input.setFocus()
        self.input.setText(DRAFTS.get(key, ""))

    def _hist_retry(self, key):
        try:
            if self.peer != key or self.cache.get(key) or key == "saved":
                return
            if key.startswith("g"):
                self.send_pkt({"type": "group_history", "group": int(key[1:])})
            elif key.startswith("c") and key[1:].isdigit():
                self.send_pkt({"type": "channel_history", "channel": int(key[1:])})
            else:
                self.send_pkt({"type": "history", "peer": key})
        except Exception:
            pass
    
    def _pres_poll(self):
        try:
            p = self.peer
            if p and not str(p).startswith("g") and p != "saved":
                self.send_pkt({"type": "presence_query", "user": p})
        except Exception:
            pass
    
    def on_typing(self, _text):
        try:
            self._emo_check(_text)
        except Exception:
            pass
        try:
            if not self.peer or self.peer.startswith("g") or self.peer == "saved":
                return
            now = time.time()
            if now - self._last_typing_sent > 1.2:
                self._last_typing_sent = now
                self.send_pkt({"type": "typing", "to": self.peer})
        except Exception:
            pass
    def update_status(self):
        if self.peer == "saved":
            self.status_lbl.setText("твои личные заметки")
            self.status_lbl.setStyleSheet(f"color:{CUR['muted']}; font-size:12px;")
            return
        if self.peer and self.peer.startswith("c") and self.peer[1:].isdigit():
            c = self.chats.get(self.peer, {})
            n = len(c.get("members", []))
            own = c.get("owner") == self.me
            self.status_lbl.setText(("твой канал · " if own else "канал · ") + str(n) + " подписчиков")
            self.status_lbl.setStyleSheet(f"color:{CUR['muted']}; font-size:12px;")
            return
        
            return
        
            return
        
        if self.peer and self.peer.startswith("g"):
            c = self.chats.get(self.peer, {})
            n = len(c.get("members", []))
            self.status_lbl.setText(f"{n} участников")
            self.status_lbl.setStyleSheet(f"color:{CUR['muted']}; font-size:12px;")
            return
        online = self.chats.get(self.peer, {}).get("online", False)
        if online:
            self.status_lbl.setText("в сети")
            self.status_lbl.setStyleSheet("color:#2ecc71; font-size:12px;")
        else:
            ls = self.last_seen.get(self.peer)
            self.status_lbl.setText(f"был(а) в сети в {ls}" if ls else "не в сети")
            self.status_lbl.setStyleSheet(f"color:{CUR['muted']}; font-size:12px;")

    # ---------- сообщения ----------
    def add_bubble(self, text, ts, mine, media="", sender_name="",
                   voice="", vdur=0.0, video="", transcript="", reply_name="",
                   reply_text="", fwd="", file_name="", file_data="", edited=False,
                   poll="", animate=True, ttl=0):
        row = QWidget()
        h = QHBoxLayout(row)
        h.setContentsMargins(0, 0, 0, 0)
        h.setSpacing(0)
        b = MessageBubble(text, ts, mine, media, sender_name, voice, vdur, video,
                          transcript, reply_name, reply_text, fwd, file_name, file_data, edited, poll)
        self._bind_bubble(b)
        if mine:
            h.addStretch(1)
            h.addWidget(b)
            if self.peer:
                self.my_bubbles.setdefault(self.peer, []).append(b)
        else:
            h.addWidget(b)
            h.addStretch(1)
        self._insert_day_sep(ts)
        was_bottom = self._at_bottom()
        self.msg_l.insertWidget(self.msg_l.count() - 1, row)
        if not was_bottom and animate:
         self._missed = getattr(self, "_missed", 0) + 1
         self._upd_down_btn()
        if animate:
         self.animate_bubble(b)
        if was_bottom:
         self.scroll_to_bottom()
         if animate:
          QTimer.singleShot(300, self.scroll_to_bottom)
        return b

    def animate_bubble(self, b):
        self.msg_l.activate()
        w = b.width() if b.width() > 0 else 300
        target = b.heightForWidth(w) if b.hasHeightForWidth() else b.sizeHint().height()
        target = max(target or 0, 44)
        b.setMaximumHeight(0)
        eff = QGraphicsOpacityEffect(b)
        b.setGraphicsEffect(eff)
        g = QParallelAnimationGroup(b)
        a1 = QPropertyAnimation(b, b"maximumHeight", b)
        a1.setDuration(300)
        a1.setStartValue(0)
        a1.setEndValue(target)
        a1.setEasingCurve(QEasingCurve.OutBack)
        a2 = QPropertyAnimation(eff, b"opacity", b)
        a2.setDuration(280)
        a2.setStartValue(0.0)
        a2.setEndValue(1.0)
        g.addAnimation(a1)
        g.addAnimation(a2)
        g.finished.connect(lambda: (b.setMaximumHeight(16777215), b.setGraphicsEffect(None)))
        b._anim = g
        g.start()

    def _stop_anims(self, w):
        try:
            for ch in [w] + list(w.findChildren(QWidget)):
                for a in (getattr(ch, "_anim", None), getattr(ch, "_fade_anim", None), getattr(ch, "_slide", None)):
                    if a is not None:
                        try:
                            a.stop()
                        except Exception:
                            pass
        except Exception:
            pass

    def clear_messages(self):
        for _it in range(self.msg_l.count()):
            _li = self.msg_l.itemAt(_it)
            _w = _li.widget() if _li else None
            if _w is None:
                continue
            for _c in [_w] + list(_w.findChildren(QWidget)):
                for _an in (getattr(_c, "_anim", None), getattr(_c, "_fade_anim", None), getattr(_c, "_slide", None)):
                    if _an is not None:
                        try:
                            _an.stop()
                        except Exception:
                            pass
        while self.msg_l.count() > 1:
            item = self.msg_l.takeAt(0)
            if item.widget():
                self._stop_anims(item.widget())
                item.widget().deleteLater()
        self.my_bubbles = {}
        self.bubbles_by_id = {}

    def _at_bottom(self):
        bar = self.scroll.verticalScrollBar()
        return bar.value() >= bar.maximum() - 40
    def _upd_down_btn(self):
        b = getattr(self, "down_btn", None)
        if b is None:
            return
        if self.stack.currentIndex() == 0 or self._at_bottom():
            self._missed = 0
            b.hide()
            return
        b.show()
        b.raise_()
        pw = self.pane.width() if getattr(self, "pane", None) else self.width()
        ph = self.pane.height() if getattr(self, "pane", None) else self.height()
        b.move(pw - 56, ph - 120)
        b.setText(("↓" + str(self._missed)) if self._missed else "↓")
    def _down_click(self):
        self._missed = 0
        self.scroll_to_bottom()
        self._upd_down_btn()

    def _safe_down(self):
        try:
            self._upd_down_btn()
        except Exception:
            pass

    def scroll_to_bottom(self, delay=0):
        def do():
            bar = self.scroll.verticalScrollBar()
            bar.setValue(bar.maximum())
        if delay:
            QTimer.singleShot(delay, do)
        else:
            do()

    def _day_label(self, ts):
     try:
      dt = datetime.fromisoformat(ts)
     except Exception:
      return None
     now = datetime.now()
     if dt.date() == now.date():
      return "Сегодня"
     if (now.date() - dt.date()).days == 1:
      return "Вчера"
     M = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]
     return f"{dt.day} {M[dt.month - 1]}"
    def _insert_day_sep(self, ts):
     lb = self._day_label(ts)
     if not lb or lb == getattr(self, "_last_day", None):
      return
     self._last_day = lb
     w = QLabel(lb)
     w.setAlignment(Qt.AlignCenter)
     w.setStyleSheet("color:" + CUR["muted"] + ";font-size:11px;font-weight:700;background:transparent;")
     self.msg_l.insertWidget(self.msg_l.count() - 1, w)
    def _insert_new_line(self):
     w = QLabel("─── Новые сообщения ───")
     w.setAlignment(Qt.AlignCenter)
     w.setStyleSheet("color:" + CUR["accent"] + ";font-size:11px;font-weight:700;background:transparent;")
     self.msg_l.insertWidget(self.msg_l.count() - 1, w)
    def _upd_pin_bar(self):
     lst = PINS_MSG.get(str(self.peer), []) if self.peer else []
     if not lst:
      self.pin_bar.hide()
      return
     mid = lst[-1]
     m = next((x for x in self.cache.get(self.peer, []) if x.get("id") == mid), None)
     self.pin_lbl.setText((m.get("text") or "📷 Вложение")[:60] if m else "Закреплено")
     self.pin_bar.show()
    def _unpin_cur(self):
     PINS_MSG.pop(str(self.peer), None)
     save_extra()
     self._upd_pin_bar()
    def _jump_pin(self):
     lst = PINS_MSG.get(str(self.peer), [])
     if not lst:
      return
     b = self.bubbles_by_id.get(lst[-1])
     if b is not None:
      self.scroll.ensureWidgetVisible(b, 60, 60)
      fade_in(b, 250)
    def _emo_check(self, text):
     import re as _re
     m = _re.search(r":([a-z0-9_]{2,12})$", text or "", _re.I)
     if not m or not getattr(self, "emo_popup", None):
      return
     q = m.group(1).lower()
     hits = [(k, v) for k, v in EMOJI_NAMES.items() if k.startswith(q)][:8]
     if not hits:
      self.emo_popup.hide()
      return
     self.emo_popup.clear()
     for k, v in hits:
      it = QListWidgetItem(v + "  :" + k + ":")
      it.setData(Qt.UserRole, v)
      self.emo_popup.addItem(it)
     self.emo_popup.setFixedHeight(min(110, 26 * len(hits) + 6))
     self.emo_popup.move(self.input.x(), self.input.y() - self.emo_popup.height() - 4)
     self.emo_popup.show()
     self.emo_popup.raise_()
    def _emo_pick(self, it):
     import re as _re
     emo = it.data(Qt.UserRole)
     t = _re.sub(r":([a-z0-9_]{2,12})$", emo, self.input.text(), flags=_re.I)
     self.input.setText(t)
     self.emo_popup.hide()
     self.input.setFocus()
    
    def set_folder(self, f):
        self.folder = f
        for fid, bb in getattr(self, "_folder_btns", {}).items():
            bb.setProperty("mine", "true" if fid == f else "false")
            bb.style().unpolish(bb)
            bb.style().polish(bb)
        self.refresh_order()

    def refresh_order(self):
        q = self.search.text().strip().lower()
        names = [n for n in self.chats if n in self.items and n != "saved" and n not in DELETED]
        names.sort(key=lambda n: self.chats[n]["ts"] or "", reverse=True)
        names.sort(key=lambda n: not self.chats[n]["online"])
        names.sort(key=lambda n: n not in PINNED)
        for n in names:
            self.list_l.removeWidget(self.items[n])
        if "saved" in self.items:
            self.list_l.removeWidget(self.items["saved"])
            self.list_l.insertWidget(0, self.items["saved"])
            self.items["saved"].setVisible(getattr(self, "folder", "all") in ("all", "personal"))
        fol = getattr(self, "folder", "all")
        def _fold_ok(n):
            c = self.chats[n]
            if fol == "all":
                return True
            if fol == "groups":
                return bool(c.get("is_group"))
            if fol == "personal":
                return not c.get("is_group")
            if fol == "unread":
                return int(c.get("unread") or 0) > 0
            return True
        for i, n in enumerate(names):
            it = self.items[n]
            disp = self.chats[n]["display"].lower()
            it.set_display(("📌 " if n in PINNED else "") + self.chats[n]["display"])
            it.setVisible(n not in DELETED and _fold_ok(n) and (q == "" or q in disp or q in n.lower()))
            self.list_l.insertWidget(i + 1, it)

        try:
            self.app.update_badge_icon()
        except Exception:
            pass
    def reset(self):
        for n, it in list(self.items.items()):
            self.list_l.removeWidget(it)
            it.deleteLater()
        self.items.clear()
        self.chats.clear()
        self.my_bubbles.clear()
        self.bubbles_by_id.clear()
        self.story_data.clear()
        self.cache.clear()
        self.peer = None
        self.clear_messages()
        self.stack.setCurrentIndex(0)
        self._set_input_vis(False)
        self.peer_name.setText("")
        self.status_lbl.setText("")


# ================== СЕТЬ ==================

class NetThread(QThread):
    packet = Signal(dict)
    lost = Signal()

    def __init__(self):
        super().__init__()
        self.sock = None
        self._run = False
        self.last_rx = 0.0

    def connect_to(self, host, port):
        self.sock = socket.create_connection((host, port), timeout=5)
        self.sock.settimeout(None)
        self._run = True
        self.start()

    def run(self):
        buf = b""
        try:
            while self._run:
                data = self.sock.recv(1024 * 1024)
                if not data:
                    break
                self.last_rx = time.time()
                buf += data
                while b"\n" in buf:
                    line, buf = buf.split(b"\n", 1)
                    if not line.strip():
                        continue
                    try:
                        _obj = json.loads(line.decode("utf-8"))
                        self.packet.emit(_obj)
                    except Exception:
                        pass
        except OSError:
            pass
        if self._run:
            self.lost.emit()

    def send(self, obj):
        try:
            self.sock.sendall((json.dumps(obj, ensure_ascii=False) + "\n").encode("utf-8"))
        except Exception:
            pass

    def close(self):
        self._run = False
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        try:
            self.sock.close()
        except Exception:
            pass


# ================== ГЛАВНОЕ ОКНО ==================

class PageBG(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._wt = QTimer(self)
        self._wt.setInterval(33)
        self._wt.timeout.connect(self.update)
        self._wt.start()
    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        paint_wallpaper(p, self.width(), self.height())
        p.end()
import base64 as _b64m
from PySide6.QtCore import QIODevice, QBuffer


class Pipe(QIODevice):
    def __init__(self):
        super().__init__(None)
        self.q = QByteArray()
        self.open(QIODevice.ReadOnly | QIODevice.Unbuffered)

    def push(self, b):
        self.q.append(QByteArray(b))

    def bytesAvailable(self):
        return len(self.q) + super().bytesAvailable()

    def readData(self, n):
        take = self.q.left(n)
        self.q.remove(0, len(take))
        return bytes(take)

    def writeData(self, b):
        return len(b)


class CallDialog(QDialog):
    def __init__(self, parent, sender, peer, peer_name, video, incoming=False):
        super().__init__(parent)
        self.sender_fn = sender
        self.peer = peer
        self.video = video
        self.setWindowTitle("Видеозвонок" if video else "Звонок")
        self.resize(480, 620)
        self.setStyleSheet(f"background:{CUR['bg']};")
        v = QVBoxLayout(self)
        self.name_lbl = QLabel(peer_name)
        self.name_lbl.setStyleSheet("font-size:20px;font-weight:700;")
        self.name_lbl.setAlignment(Qt.AlignCenter)
        self.stat_lbl = QLabel("Входящий звонок..." if incoming else "Звоним...")
        self.stat_lbl.setStyleSheet(f"color:{CUR['muted']};")
        self.stat_lbl.setAlignment(Qt.AlignCenter)
        self.remote = QLabel("📞")
        self.remote.setAlignment(Qt.AlignCenter)
        self.remote.setMinimumHeight(300)
        self.remote.setStyleSheet(f"border-radius:12px;background:{CUR['card']};")
        v.addWidget(self.name_lbl)
        v.addWidget(self.stat_lbl)
        v.addWidget(self.remote)
        row = QHBoxLayout()
        row.addStretch(1)
        if incoming:
            self.ok_btn = QPushButton("Принять")
            self.ok_btn.setObjectName("primaryBtn")
            self.ok_btn.clicked.connect(self.accept_call)
            row.addWidget(self.ok_btn)
        self.end_btn = QPushButton("Завершить")
        self.end_btn.setObjectName("ghostBtn")
        self.end_btn.clicked.connect(self.hangup)
        row.addWidget(self.end_btn)
        row.addStretch(1)
        v.addLayout(row)
        self.active = False
        self.player_pipe = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.pump_audio)
        self.vtimer = QTimer(self)
        self.vtimer.timeout.connect(self.send_frame)

    def send(self, extra):
        pkt = {"to": self.peer}
        pkt.update(extra)
        self.sender_fn(pkt)

    def notify_incoming(self):
        try:
            from PySide6.QtCore import QUrl
            from PySide6.QtMultimedia import QSoundEffect
            self.ring = QSoundEffect()
            self.ring.setSource(QUrl.fromLocalFile(make_pop_wav()))
            self.ring.setLoopCount(QSoundEffect.Infinite)
            self.ring.play()
        except Exception:
            pass

    def stop_ring(self):
        try:
            if getattr(self, "ring", None):
                self.ring.stop()
        except Exception:
            pass

    def accept_call(self):
        self.stop_ring()
        self.send({"type": "call_answer"})
        self.start_media()

    def on_pkt(self, pkt):
        t = pkt["type"]
        if t == "call_answer":
            self.stop_ring()
            self.start_media()
        elif t == "call_end":
            self.close()
        elif t == "call_audio" and self.player_pipe is not None:
            try:
                self.player_pipe.push(_b64m.b64decode(pkt.get("data") or ""))
            except Exception:
                pass
        elif t == "call_video":
            try:
                img = QImage()
                img.loadFromData(_b64m.b64decode(pkt.get("data") or ""))
                if not img.isNull():
                    self.remote.setPixmap(QPixmap.fromImage(img).scaled(
                        self.remote.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            except Exception:
                pass

    def start_media(self):
        if self.active:
            return
        self.active = True
        self.stat_lbl.setText("Разговор")
        from PySide6.QtMultimedia import QAudioSource, QAudioSink, QAudioFormat
        fmt = QAudioFormat()
        fmt.setSampleRate(16000)
        fmt.setChannelCount(1)
        fmt.setSampleFormat(QAudioFormat.Int16)
        self.sink = QAudioSink(fmt)
        self.player_pipe = Pipe()
        self.sink.start(self.player_pipe)
        self.src = QAudioSource(fmt)
        self.mic_io = self.src.start()
        self.timer.start(100)
        if self.video:
            try:
                from PySide6.QtMultimedia import QMediaCaptureSession, QCamera, QVideoSink, QMediaDevices
                self.session = QMediaCaptureSession()
                self.cam = QCamera(QMediaDevices.defaultVideoInput())
                self.session.setCamera(self.cam)
                self.vsink = QVideoSink()
                self.session.setVideoOutput(self.vsink)
                self.vsink.videoFrameChanged.connect(self.on_frame)
                self.cam.start()
                self.vtimer.start(250)
            except Exception as ex:
                print("CAM ERR:", ex)

    def on_frame(self, frame):
        self.last_frame = frame

    def send_frame(self):
        f = getattr(self, "last_frame", None)
        if f is None:
            return
        try:
            img = f.toImage().scaledToWidth(320)
            buf = QBuffer()
            buf.open(QIODevice.WriteOnly)
            img.save(buf, "JPG", 50)
            self.send({"type": "call_video", "data": _b64m.b64encode(bytes(buf.data())).decode()})
        except Exception:
            pass

    def pump_audio(self):
        try:
            d = self.mic_io.readAll()
        except Exception:
            return
        if d:
            self.send({"type": "call_audio", "data": _b64m.b64encode(bytes(d)).decode()})

    def hangup(self):
        self.send({"type": "call_end"})
        self.close()

    def closeEvent(self, e):
        try:
            self.stop_ring()
            self.timer.stop()
            self.vtimer.stop()
            if getattr(self, "src", None):
                self.src.stop()
            if getattr(self, "sink", None):
                self.sink.stop()
            if getattr(self, "cam", None):
                self.cam.stop()
        except Exception:
            pass
        super().closeEvent(e)


def _wa_geo(win, target, dur=220):
    try:
        a = QPropertyAnimation(win, b"geometry")
        a.setDuration(dur)
        a.setStartValue(win.geometry())
        a.setEndValue(target)
        a.setEasingCurve(QEasingCurve.OutCubic)
        win._wa_geo_anim = a
        a.start()
    except Exception:
        win.setGeometry(target)
def _wa_restore_pop(w):
    try:
        g = w.geometry()
        dw = int(g.width() * 0.05)
        dh = int(g.height() * 0.05)
        start = g.adjusted(dw, dh, -dw, -dh)
        w.setWindowOpacity(0.0)
        w.setGeometry(start)
        a1 = QPropertyAnimation(w, b"windowOpacity")
        a1.setDuration(220)
        a1.setStartValue(0.0)
        a1.setEndValue(1.0)
        a2 = QPropertyAnimation(w, b"geometry")
        a2.setDuration(220)
        a2.setStartValue(start)
        a2.setEndValue(g)
        a2.setEasingCurve(QEasingCurve.OutCubic)
        grp = QParallelAnimationGroup(w)
        grp.addAnimation(a1)
        grp.addAnimation(a2)
        w._wa_restore_grp = grp
        grp.start()
    except Exception:
        pass

class TitleBar(QWidget):
    def __init__(self, win):
        super().__init__()
        self.win = win
        self.setObjectName("titlebar")
        self.setFixedHeight(42)
        h = QHBoxLayout(self)
        h.setContentsMargins(12, 0, 8, 0)
        h.setSpacing(8)
        h.addStretch(1)
        self.min_b = IconBtn("min", 26)
        self.max_b = IconBtn("max", 26)
        self.close_b = IconBtn("close", 26)
        for b in (self.min_b, self.max_b, self.close_b):
            b.setFixedSize(36, 28)
        self.min_b.clicked.connect(self.anim_min)
        self.max_b.clicked.connect(self.toggle_max)
        self.close_b.clicked.connect(self.close_win)
        h.addWidget(self.min_b)
        h.addWidget(self.max_b)
        h.addWidget(self.close_b)

    def toggle_max(self):
        w = self.win
        try:
            scr = QApplication.primaryScreen().availableGeometry()
        except Exception:
            scr = None
        if scr is None:
            return
        if getattr(w, "_wa_maxed", False):
            tgt = getattr(w, "_wa_normal", None) or w.geometry()
            w._wa_maxed = False
            _wa_geo(w, tgt)
        else:
            w._wa_normal = w.geometry()
            w._wa_maxed = True
            _wa_geo(w, scr)
    def anim_min(self):
        w = self.win
        if getattr(w, "_wa_min_busy", False):
            return
        w._wa_min_busy = True
        w._was_min = True
        a = QPropertyAnimation(w, b"windowOpacity")
        a.setDuration(150)
        a.setStartValue(w.windowOpacity())
        a.setEndValue(0.0)
        a.setEasingCurve(QEasingCurve.InCubic)
        def _fin():
            try:
                w.setWindowOpacity(1.0)
                w.showMinimized()
            finally:
                w._wa_min_busy = False
        a.finished.connect(_fin)
        w._wa_min_anim = a
        a.start()

    def close_win(self):
        w = self.win
        fa = QPropertyAnimation(w, b"windowOpacity")
        fa.setDuration(220)
        fa.setStartValue(w.windowOpacity())
        fa.setEndValue(0.0)
        fa.finished.connect(w.close)
        fa.start()
        w._fade = fa

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton and self.win.windowHandle():
            wh = self.win.windowHandle()
            if wh is not None:
                wh.startSystemMove()

    def mouseDoubleClickEvent(self, e):
        self.toggle_max()


class Messenger(QStackedWidget):
    def __init__(self, server_ok=True):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint | Qt.WindowSystemMenuHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.connected = False
        self.authed = False
        self.creds = ("", "")
        self.net = None
        self.auth = AuthScreen()
        self.auth.submit.connect(self.on_auth_submit)
        self.chat = ChatScreen(self)
        self.auth_w = PageBG()
        aw = QVBoxLayout(self.auth_w)
        aw.setContentsMargins(0, 0, 0, 0)
        aw.setSpacing(0)
        aw.addWidget(TitleBar(self))
        aw.addWidget(self.auth)
        self.chat_w = PageBG()
        cw2 = QVBoxLayout(self.chat_w)
        cw2.setContentsMargins(0, 0, 0, 0)
        cw2.setSpacing(0)
        cw2.addWidget(TitleBar(self))
        cw2.addWidget(self.chat)
        self.addWidget(self.auth_w)
        self.addWidget(self.chat_w)
        self.lock_w = PageBG()
        lw = QVBoxLayout(self.lock_w)
        lw.setContentsMargins(0, 0, 0, 0)
        lw.setSpacing(0)
        lw.addWidget(TitleBar(self))
        self.lock_scr = LockScreen()
        self.lock_scr.unlocked.connect(self._on_unlocked)
        self.lock_scr.forgot.connect(self.forgot_lock)
        lw.addWidget(self.lock_scr)
        self.addWidget(self.lock_w)
        self.locked = False
        if not server_ok:
            self.auth.set_status("Не нашёл server.py — положи его рядом с client.py")
        self.reconnect_t = QTimer(self)
        self.reconnect_t.setInterval(3000)
        self.reconnect_t.timeout.connect(self.try_reconnect)
        self.watch_t = QTimer(self)
        self.watch_t.setInterval(5000)
        self.watch_t.timeout.connect(self._watchdog)
        self.watch_t.start()
        self.tray = QSystemTrayIcon(self._make_icon(), self)
        self.tray.setToolTip("Bebsi")
        self.tray.show()
        self.pop = QSoundEffect()
        self.pop.setSource(QUrl.fromLocalFile(make_pop_wav()))

    def changeEvent(self, e):
        try:
            QStackedWidget.changeEvent(self, e)
        except Exception:
            pass
        try:
            if e.type() == QEvent.WindowStateChange:
                if not (self.windowState() & Qt.WindowMinimized) and getattr(self, "_was_min", False):
                    self._was_min = False
                    _wa_restore_pop(self)
        except Exception:
            pass

    def _make_icon(self):
        px = QPixmap(64, 64)
        px.fill(Qt.transparent)
        p = QPainter(px)
        p.setRenderHint(QPainter.Antialiasing)
        g = QLinearGradient(0, 0, 64, 64)
        g.setColorAt(0, QColor(CUR["accent"]))
        g.setColorAt(1, QColor(CUR["accent2"]))
        p.setBrush(g); p.setPen(Qt.NoPen)
        p.drawEllipse(2, 2, 60, 60)
        p.setPen(QColor("#ffffff"))
        f = p.font(); f.setBold(True); f.setPixelSize(34)
        p.setFont(f)
        p.drawText(0, 0, 64, 64, Qt.AlignCenter, "B")
        p.end()
        return QIcon(px)

    
    def _tb_restore(self):
        try:
            self.show()
            self.raise_()
            self.activateWindow()
        except Exception:
            pass

    def _call_send(self, pkt):
        if self.net:
            self.net.send(pkt)

    def handle_call(self, pkt):
        print("CALL PKT:", pkt.get("type"))
        frm = pkt.get("from") or ""
        if pkt["type"] == "call_offer":
            self.call = CallDialog(self, self._call_send, frm, frm, bool(pkt.get("video")), incoming=True)
            self.call.show()
            self.call.notify_incoming()
        elif getattr(self, "call", None) is not None and self.call.peer == frm:
            self.call.on_pkt(pkt)

    def notify(self, pkt):
        global LAST_U
        frm = pkt.get("from") or ""
        if frm == self.chat.me:
            return
        cur = None
        for v in list(self.__dict__.values()):
            if hasattr(v, "peer") and hasattr(v, "start_call"):
                cur = v.peer
                break
        if cur == frm and self.isActiveWindow() and not self.isMinimized():
            return
        if frm in MUTES or dnd_active():
            return
        name = self.chat.chats.get(frm, {}).get("display", frm)
        txt = pkt.get("text") or ("🎤 Голосовое" if pkt.get("voice") else
              "⭕ Кружок" if pkt.get("video") else "📷 Фото" if pkt.get("media") else
              "Опрос" if pkt.get("poll") else "📄 Файл" if pkt.get("file_data") else "💬")
        if not SOUND_ON:
            return
        self.pop.play()

    def make_net(self):
        old = self.net
        if old is not None:
            try:
                old.close()
            except Exception:
                pass
            try:
                old.wait(2000)
            except Exception:
                pass
        self.net = NetThread()
        self.net.packet.connect(self.on_packet)
        self.net.lost.connect(self.on_lost)

    def paintEvent(self, _):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        g = QLinearGradient(0, 0, 0, self.height())
        g.setColorAt(0, QColor(CUR["bg"]))
        g.setColorAt(1, QColor(CUR["panel"]))
        p.fillRect(self.rect(), QBrush(g))
        p.setPen(Qt.NoPen)
        c1 = QColor(CUR["accent"])
        c1.setAlpha(35)
        p.setBrush(c1)
        p.drawEllipse(QPointF(self.width() * 0.9, self.height() * 0.1), 220, 220)
        c2 = QColor("#00cec9")
        c2.setAlpha(25)
        p.setBrush(c2)
        p.drawEllipse(QPointF(self.width() * 0.1, self.height() * 0.9), 240, 240)

    def on_auth_submit(self, mode, u, p):
        self._kicked = False
        self.creds = (u, p)
        if not self.connected:
            try:
                self.make_net()
                self.net.connect_to(SERVER_HOST, SERVER_PORT)
                self.connected = True
            except Exception:
                self.auth.error("Сервер не отвечает — запусти server.py и попробуй ещё")
                return
        self.auth.set_status("Секундочку…")
        self.net.send({"type": mode, "username": u, "password": p, "email": (self.auth.e.text().strip().lower() if mode == "register" else ""), "device": _device_name(), "platform": sys.platform})

    def show_update(self, pkt):
        from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
        if pkt.get("hash") == getattr(self, "_declined_hash", None):
            return
        d = QDialog(self)
        v = QVBoxLayout(d)
        v.setContentsMargins(24, 24, 24, 24)
        v.setSpacing(12)
        lb = QLabel("🚀 Доступна новая версия Bebsi!")
        lb.setObjectName("title")
        v.addWidget(lb)
        b = QPushButton("🔄 Обновить")
        b.setObjectName("bubbleMine")
        b.clicked.connect(d.accept)
        v.addWidget(b)
        b2 = QPushButton("Позже")
        b2.setObjectName("ghostBtn")
        b2.clicked.connect(d.reject)
        v.addWidget(b2)
        if d.exec() == QDialog.Accepted:
            try:
                import base64, os, subprocess
                raw = base64.b64decode(pkt["data"])
                p = os.path.abspath(__file__)
                with open(p, "wb") as f:
                    f.write(raw)
                if getattr(sys, "frozen", False):
                    try:
                        _do_self_restart()
                    except Exception:
                        pass
                else:
                    subprocess.Popen([sys.executable, p], cwd=os.path.dirname(p))
                os._exit(0)
            except Exception as ex:
                print("update err:", ex)
        else:
            self._declined_hash = pkt.get("hash")

    def _chan_packet(self, pkt, t):
        if t == "channels":
            self.chat.handle_channels(pkt.get("channels") or [])
            return True
        if t == "channels_changed":
            self.net.send({"type": "channels"})
            return True
        if t == "channel_search":
            self.show_channel_results(pkt.get("channels") or [])
            return True
        if t == "channel_message":
            e = self.chat._extra(pkt)
            self.chat.incoming_channel_message(pkt["channel"], pkt["from"], pkt["text"], pkt.get("ts", ""), pkt.get("id"), pkt.get("reactions"), **e)
            if (pkt.get("from") or "") != self.chat.me:
                self.show_toast(pkt)
            return True
        if t == "channel_history":
            self.chat.handle_channel_history(pkt["channel"], pkt.get("messages") or [])
            return True
        return False
    
    def on_packet(self, pkt):
        t = pkt.get("type")
        if self._chan_packet(pkt, t):
            return
        if t in ("update_ok", "update_avail"):
            try:
                self.chat._upd_resp_at = time.time()
            except Exception:
                pass
        if pkt.get("type") == "message" and (pkt.get("from") or "") != self.chat.me:
            self.notify(pkt)
        elif t == "update_avail":
            _upd_dbg("GOT update_avail")
            self.chat.show_update(pkt)
        t = pkt.get("type")
        if t == "auth_ok":
            global LAST_U
            self.authed = True
            self._reconn_n = 0
            try:
                self.auth._anim_t.stop()
            except Exception:
                pass
            try:
                LAST_U = pkt["username"]
                if self.creds and not any(a["u"] == pkt["username"] for a in ACCOUNTS):
                    if len(ACCOUNTS) < 3:
                        ACCOUNTS.append({"u": pkt["username"], "p": _dpapi_protect((self.creds[1] or "").encode("utf-8"))})
                save_settings()
                try:
                    _same = getattr(self.chat, "me", None) == pkt["username"]
                except Exception:
                    _same = False
                self._reconn_n = 0
                self._last_auth_at = time.time()
                if not _same:
                    if getattr(self.chat, "me", None) != pkt.get("username"):
                        try:
                            _old = self.chat
                            _old.upd_timer.stop()
                            _old.typing_timer.stop()
                            _old.rec_timer.stop()
                            self.chat_w.layout().removeWidget(_old)
                            _old.setParent(None)
                            QTimer.singleShot(500, _old.deleteLater)
                        except Exception:
                            pass
                        self.chat = ChatScreen(self)
                        try:
                            self.chat_w.layout().addWidget(self.chat)
                        except Exception:
                            pass
                QTimer.singleShot(1500, self.request_all_history)
                self.chat.set_me(pkt["username"], pkt)
                self.chat.my_email = pkt.get("email", "") or ""
                QTimer.singleShot(1500, self._auto_open)
                if getattr(self, "locked", False) and LOCK_HASH:
                    self.setCurrentWidget(self.lock_w)
                else:
                    self.setCurrentWidget(self.chat_w)
                try:
                    fade_in(self.chat_w)
                except Exception:
                    pass
                self.net.send({"type": "users"})
                self.net.send({"type": "groups"})
                self.net.send({"type": "channels"})
            except Exception as _e:
                _upd_dbg("AUTH_OK ERR " + repr(_e))
                try:
                    self.auth.error("Ошибка входа: " + repr(_e))
                except Exception:
                    pass
        elif t == "kicked":
            self._kicked = True
            self.reconnect_t.stop()
            self.connected = False
            self.authed = False
            try:
                self.auth.error("С этого аккаунта вошли с другого устройства — соединение закрыто")
            except Exception:
                pass
            self.setCurrentIndex(0)
            return
        elif t == "error":
            if not self.authed:
                self.auth.error(pkt.get("message", "Ошибка"))
            else:
                dlg = getattr(self, "email_dlg", None)
                if dlg is not None:
                    dlg.show_err(pkt.get("message", "Ошибка"))
                else:
                    self.chat.show_warn(pkt.get("message", "Ошибка"))
        elif t == "users":
            self.chat.handle_users(pkt["users"], pkt.get("chats"))
        elif t == "presence":
            self.chat.handle_presence(pkt["user"], pkt["online"])
        elif t == "profile":
            self.chat.handle_profile(pkt["user"], pkt["display"], pkt["bio"], pkt["avatar"])
        elif t == "groups_changed":
            self.net.send({"type": "groups"})
        elif t == "groups":
            self.chat.handle_groups(pkt["groups"])
        elif t in ("call_offer", "call_answer", "call_end", "call_audio", "call_video"):
            self.handle_call(pkt)
        elif t == "message":
            e = self.chat._extra(pkt)
            if pkt.get("ttl"):
                e["ttl"] = pkt["ttl"]
            if pkt["from"] == self.chat.me:
                to = pkt.get("to") or ""
                if not to:
                    return
                self.chat.incoming_message(pkt["from"], pkt["text"], pkt.get("ts", ""),
                    pkt.get("id"), pkt.get("reactions"), force_key=("saved" if to == self.chat.me else to), **e)
            else:
                self.chat.incoming_message(pkt["from"], pkt["text"], pkt.get("ts", ""),
                    pkt.get("id"), pkt.get("reactions"), **e)
                self.show_toast(pkt)
        elif t == "group_message":
            e = self.chat._extra(pkt)
            if pkt.get("ttl"):
                e["ttl"] = pkt["ttl"]
            self.chat.incoming_group_message(pkt["group"], pkt["from"], pkt["text"],
                pkt.get("ts", ""), pkt.get("id"),
                pkt.get("reactions"), **e)
            if (pkt.get("from") or "") != self.chat.me:
                self.show_toast(pkt)
        elif t == "ack_id":
            self.chat.on_ack_id(pkt["id"])
        elif t == "reaction":
            self.chat.on_reaction(pkt["msg_id"], pkt["reactions"])
        elif t == "edited":
            self.chat.on_edited(pkt["msg_id"], pkt["text"])
        elif t == "deleted":
            self.chat.on_deleted(pkt["msg_id"])
        elif t == "poll_update":
            self.chat.on_poll_update(pkt["msg_id"], pkt["votes"])
        elif t == "read":
            self.chat.on_read(pkt["from"])
        elif t == "search_users":
            self.show_user_results(pkt.get("users") or [])
        elif t == "history":
            _upd_dbg("HIST GOT peer=" + str(pkt.get("peer")) + " keys=" + repr(sorted(pkt.keys()))[:60])
            if pkt.get("peer") == self.chat.me:
                return
            key = "saved" if pkt["peer"] == self.chat.me else pkt["peer"]
            _upd_dbg("HIST MAP key=" + str(key))
            self.chat.handle_history(key, pkt["messages"])
        elif t == "channels":
            self.chat.handle_channels(pkt.get("channels") or [])
        elif t == "channels_changed":
            self.net.send({"type": "channels"})
        elif t == "channel_search":
            self.show_channel_results(pkt.get("channels") or [])
        elif t == "channel_message":
            e = self.chat._extra(pkt)
            self.chat.incoming_channel_message(pkt["channel"], pkt["from"], pkt["text"], pkt.get("ts", ""), pkt.get("id"), pkt.get("reactions"), **e)
            if (pkt.get("from") or "") != self.chat.me:
                self.show_toast(pkt)
        elif t == "channel_history":
            self.chat.handle_channel_history(pkt["channel"], pkt.get("messages") or [])
        
        elif t == "group_history":
            self.chat.handle_group_history(pkt["group"], pkt["messages"])
        elif t == "stories":
            self.chat.handle_stories(pkt["stories"])
        elif t == "story_new":
            self.chat.on_story_new(pkt["id"], pkt["user"], pkt["media"],
                                   pkt["caption"], pkt["ts"])
        elif t == "typing":
            self.chat.on_typing_event(pkt["from"])
        elif t == "email_code_sent":
            dlg = getattr(self, "email_dlg", None)
            if dlg is not None:
                dlg.code_sent()
        elif t == "email_set":
            self.chat.my_email = pkt.get("email", "") or ""
            dlg = getattr(self, "email_dlg", None)
            if dlg is not None:
                dlg.done_ok(self.chat.my_email)
            self.chat.show_warn("Почта привязана ✉️")
        elif t == "sessions":
         dlg = getattr(self, "devices_dlg", None)
         if dlg is not None:
          dlg.set_sessions(pkt.get("sessions") or [])

    def on_lost(self):
        self.connected = False
        try:
            with open(os.path.join(DIR, "reconnect.log"), "a", encoding="utf-8") as f:
                f.write(time.strftime("%H:%M:%S") + " lost authed=" + str(self.authed) + "\n")
        except Exception:
            pass
        if getattr(self, "_kicked", False):
            return
        if self.authed:
            self.chat.set_conn_status(False)
            self._reconn_n = getattr(self, "_reconn_n", 0) + 1
            if self._reconn_n > 6:
                self.reconnect_t.stop()
                self.authed = False
                self.setCurrentIndex(0)
                self.auth.set_status("Соединение потеряно — нажми Войти ещё раз")
                return
            self.reconnect_t.setInterval(min(3000 * self._reconn_n, 12000))
            self.reconnect_t.start()
    def try_reconnect(self):
        if getattr(self, "_reconnecting", False):
            return
        self._reconnecting = True
        try:
            if getattr(self, "_kicked", False):
                self.reconnect_t.stop()
                return
            try:
                self.make_net()
                self.net.connect_to(SERVER_HOST, SERVER_PORT)
                self.connected = True
                self.reconnect_t.stop()
                u, p = self.creds
                self.net.send({"type": "login", "username": u, "password": p})
                self.chat.set_conn_status(True)
                QTimer.singleShot(1200, self.request_all_history)
            except Exception:
                pass

        finally:
            self._reconnecting = False
    def reset_all(self):
        self.peer = None
        for w in list(self.items.values()):
            try:
                w.hide()
                w.deleteLater()
            except Exception:
                pass
        self.items.clear()
        self.chats.clear()
        self.cache.clear()
        self.my_bubbles.clear()
        self.bubbles_by_id.clear()
        self.clear_messages()
        self.stack.setCurrentIndex(0)
        self._set_input_vis(False)
        self.peer_name.setText("")
        self.status_lbl.setText("")

    def request_all_history(self):
        _upd_dbg("HIST REQ keys=" + repr(list(self.chat.chats.keys())))
        for key in list(self.chat.chats):
            try:
                if str(key).startswith("g") and str(key)[1:].isdigit():
                    self.chat.send_pkt({"type": "group_history", "group": int(str(key)[1:])})
                elif str(key).startswith("c") and str(key)[1:].isdigit():
                    self.chat.send_pkt({"type": "channel_history", "channel": int(str(key)[1:])})
                else:
                    self.chat.send_pkt({"type": "history", "peer": self.chat.me if key == "saved" else key})
            except Exception:
                pass

    def _auto_open(self):
        try:
            k = getattr(self, "last_peer", None)
            _upd_dbg("AUTOOPEN k=" + repr(k) + " chats=" + repr(list(self.chat.chats.keys())[:6]))
            if k and self.chat.peer != k and (k in self.chat.chats or k == "saved"):
                self.chat.open_chat(k)
        except Exception:
            pass
    
    def open_accounts_menu(self):
        m = QMenu(self)
        cur = getattr(self.chat, "me", None)
        acts = []
        for a in ACCOUNTS:
            mark = "✓ " if a["u"] == cur else ""
            acts.append(m.addAction(mark + str(a["u"])))
        m.addSeparator()
        dels = []
        for a in ACCOUNTS:
            dels.append(m.addAction("🗑 Удалить: " + str(a["u"])))
        if dels:
            m.addSeparator()
        add = m.addAction("➕ Добавить аккаунт") if len(ACCOUNTS) < 3 else None
        act = m.exec(QCursor.pos())
        if act is None:
            return
        if add is not None and act == add:
            self.logout()
            return
        if act in acts:
            a = ACCOUNTS[acts.index(act)]
            if a["u"] == cur:
                return
            self.logout()
            self.on_auth_submit("login", a["u"], acc_pw(a))
            return
        if act in dels:
            a = ACCOUNTS[dels.index(act)]
            ACCOUNTS.remove(a)
            global LAST_U
            if LAST_U == a["u"]:
                LAST_U = ACCOUNTS[0]["u"] if ACCOUNTS else ""
            save_settings()
            if a["u"] == cur:
                if ACCOUNTS:
                    b = ACCOUNTS[0]
                    self.logout()
                    self.on_auth_submit("login", b["u"], acc_pw(b))
                else:
                    self.logout()
            return
    def _auto_login(self):
        _upd_dbg("AUTOLOGIN ENTER last=" + repr(LAST_U) + " accounts=" + repr([a.get("u") for a in ACCOUNTS]))
        try:
            u = LAST_U or (ACCOUNTS[0]["u"] if ACCOUNTS else "")
            if not u:
                return
            a = next((x for x in ACCOUNTS if x["u"] == u), None)
            if a is None:
                return
            _upd_dbg("AUTOLOGIN as " + str(u))
            self.on_auth_submit("login", a.get("u"), acc_pw(a))
        except Exception as _e:
            _upd_dbg("AUTOLOGIN ERR " + repr(_e))

    def show_user_results(self, users):
        try:
            users = [u for u in users if u.get("name")]
            if not users:
                return
            from PySide6.QtWidgets import QMenu
            mm = QMenu(self)
            mm.setStyleSheet(f"QMenu {{ background: {CUR['card']}; border: 1px solid {CUR['stroke']}; border-radius: 10px; padding: 6px; }} QMenu::item {{ color: {CUR['text']}; padding: 7px 14px; border-radius: 7px; }} QMenu::item:selected {{ background: {rgba(CUR['accent'], 90)}; }}")
            for u in users:
                nm = u.get("name")
                dp = u.get("display") or nm
                act = mm.addAction(dp + ("  (@" + nm + ")" if nm != dp else ""))
                act.setData(nm)
            act = mm.exec(self.chat.search.mapToGlobal(QPoint(0, self.chat.search.height() + 6)))
            if act is not None:
                nm = act.data()
                self.chat.ensure_chat(nm)
                c = self.chat.chats.get(nm)
                if c is not None and not c.get("display"):
                    c["display"] = nm
                self.chat.open_chat(nm)
        except Exception:
            pass
    
    def show_channel_results(self, chs):
        try:
            if not chs:
                self.chat.show_warn("Каналы не найдены 🔍")
                return
            from PySide6.QtWidgets import QMenu
            mm = QMenu(self)
            for ch in chs:
                act = mm.addAction("📢 " + str(ch.get("name")) + " · " + str(len(ch.get("subs") or [])) + " подписч.")
                act.setData(ch)
            act = mm.exec(self.chat.search.mapToGlobal(QPoint(0, self.chat.search.height() + 6)))
            if act is not None:
                ch = act.data()
                self.chat.send_pkt({"type": "channel_sub", "id": ch.get("id"), "on": True})
                self.chat.handle_channels([ch])
                self.chat.open_chat("c" + str(ch.get("id")))
        except Exception:
            pass
    
    def show_toast(self, pkt):
        if getattr(self, "locked", False) and self.currentWidget() is getattr(self, "lock_w", None):
            return
        try:
            t = pkt.get("type")
            if t == "group_message":
                key = "g" + str(pkt.get("group"))
                c = (self.chat.chats.get(key) or {}) if self.chat else {}
                title = c.get("display") or ("Группа " + str(pkt.get("group")))
            else:
                frm = pkt.get("from") or ""
                if self.chat is not None and frm == getattr(self.chat, "me", None):
                    key, title = "saved", "Избранное"
                else:
                    key = frm
                    title = frm
                    try:
                        title = CONTACT_NAMES.get(frm) or (self.chat.all_names.get(frm) or {}).get("display") or frm
                    except Exception:
                        pass
            text = pkt.get("text") or ("📷 Фото" if pkt.get("media") else ("🎤 Голосовое" if pkt.get("voice") else ("📎 Файл" if pkt.get("file_data") else "Сообщение")))
            if self.chat is not None and getattr(self.chat, "peer", None) == key and self.isActiveWindow():
                return
            _k0 = pkt.get("from") or ""
            if pkt.get("type") == "group_message":
                _k0 = "g" + str(pkt.get("group"))
            if not TOASTS_ON or _k0 in MUTES or dnd_active():
                return
            toast = Toast(title, text, key)
            toast.clicked.connect(self._toast_click)
            toast.pop()
        except Exception:
            pass
    
    def _toast_click(self, key):
        try:
            self.chat.open_chat(key)
            self.raise_()
            self.activateWindow()
        except Exception:
            pass
    def _watchdog(self):
        try:
            if getattr(self, "_kicked", False): return
            if not (self.connected and self.authed and self.net is not None):
                return
            lr = getattr(self.net, "last_rx", 0.0) or 0.0
            if lr and (time.time() - lr > 45):
                _upd_dbg("WATCHDOG: тишина >25с -> реконнект")
                self.on_lost()
        except Exception:
            pass
    
    def forgot_lock(self):
        global LAST_U, LOCK_HASH
        ACCOUNTS.clear()
        LAST_U = ""
        LOCK_HASH = ""
        save_settings()
        self.locked = False
        try:
            self.lock_scr.code.setText("")
            self.lock_scr.status.setText("")
        except Exception:
            pass
        self.logout()
    
    def lock_now(self):
        if not LOCK_HASH:
            try:
                self.chat.show_warn("Сначала задай код-пароль в настройках 🔒")
                LockDialog(self).exec()
            except Exception:
                pass
            return
        self.locked = True
        self.setCurrentWidget(self.lock_w)
    def _on_unlocked(self):
        self.locked = False
        self.setCurrentWidget(self.chat_w if self.authed else self.auth_w)
    def show_lock(self):
        if LOCK_HASH:
            self.locked = True
            self.setCurrentWidget(self.lock_w)
    
    def update_badge_icon(self):
        try:
            total = sum(int(c.get("unread") or 0) for c in self.chat.chats.values())
            if total == getattr(self, "_badge_n", -1):
                return
            self._badge_n = total
            from PySide6.QtGui import QPixmap, QPainter, QFont
            pm = QPixmap(64, 64)
            pm.fill(Qt.transparent)
            p = QPainter(pm)
            p.setRenderHint(QPainter.Antialiasing)
            g = QLinearGradient(0, 0, 64, 64)
            g.setColorAt(0, QColor(CUR["accent"]))
            g.setColorAt(1, QColor(CUR["accent2"]))
            p.setBrush(g); p.setPen(Qt.NoPen)
            p.drawEllipse(2, 2, 60, 60)
            p.setPen(QColor("#ffffff"))
            f = p.font(); f.setBold(True); f.setPixelSize(34)
            p.setFont(f)
            p.drawText(0, 0, 64, 64, Qt.AlignCenter, "B")
            if total > 0:
                p.setPen(Qt.NoPen)
                p.setBrush(QColor("#ff5e7d"))
                p.drawEllipse(38, 2, 24, 24)
                p.setPen(QColor("#ffffff"))
                f2 = p.font(); f2.setBold(True); f2.setPixelSize(14)
                p.setFont(f2)
                p.drawText(38, 2, 24, 24, Qt.AlignCenter, str(total if total < 100 else "99"))
            p.end()
            ic = QIcon(pm)
            self.setWindowIcon(ic)
            try:
                self.tray.setIcon(ic)
            except Exception:
                pass
        except Exception:
            pass
    def logout(self):
        self.authed = False
        self.creds = ("", "")
        self.connected = False
        old = self.net
        self.net = None
        if old is not None:
            try:
                old.close()
            except Exception:
                pass
            try:
                old.wait(2000)
            except Exception:
                pass
        try:
            self.chat.upd_timer.stop()
            self.chat.typing_timer.stop()
            self.chat.rec_timer.stop()
        except Exception:
            pass
        try:
            self.auth.u.setText("")
            self.auth.p.setText("")
            self.auth._entered = False
        except Exception:
            pass
        self.setCurrentIndex(0)
    def closeEvent(self, e):
        self.reconnect_t.stop()
        if self.chat.recorder is not None:
            self.chat.recorder.stop()
        if self.net:
            self.net.close()
        super().closeEvent(e)


_upd_dbg("BUILD MARK P4")
print("BEBSI CLIENT LOADED:", __file__)


def _enable_blur(hwnd):
    import ctypes
    class ACCENT_POLICY(ctypes.Structure):
        _fields_ = [("AccentState", ctypes.c_uint), ("AccentFlags", ctypes.c_uint),
                    ("GradientColor", ctypes.c_uint), ("AnimationId", ctypes.c_uint)]
    class WCA_DATA(ctypes.Structure):
        _fields_ = [("Attribute", ctypes.c_int), ("Data", ctypes.POINTER(ctypes.c_int)),
                    ("SizeOfData", ctypes.c_size_t)]
    accent = ACCENT_POLICY()
    accent.AccentState = 3
    accent.GradientColor = 0x6612141C
    data = WCA_DATA()
    data.Attribute = 19
    data.Data = ctypes.cast(ctypes.byref(accent), ctypes.POINTER(ctypes.c_int))
    data.SizeOfData = ctypes.sizeof(accent)
    ctypes.windll.user32.SetWindowCompositionAttribute(hwnd, ctypes.byref(data))


def make_icon():
    from PySide6.QtGui import QPixmap, QPainter, QLinearGradient, QBrush, QFont, QPolygon
    from PySide6.QtCore import QRect
    pm = QPixmap(256, 256)
    pm.fill(Qt.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.Antialiasing)
    g = QLinearGradient(0, 0, 256, 256)
    g.setColorAt(0, QColor(CUR["accent"]))
    g.setColorAt(1, QColor(CUR["accent2"]))
    p.setBrush(QBrush(g))
    p.setPen(Qt.NoPen)
    p.drawRoundedRect(8, 8, 240, 240, 60, 60)
    p.setBrush(QColor(255, 255, 255, 235))
    p.drawRoundedRect(52, 66, 152, 104, 32, 32)
    p.drawPolygon(QPolygon([QRect(78, 160, 34, 40).bottomLeft(), QRect(78, 160, 34, 40).topLeft(), QRect(78, 160, 34, 40).topRight()]))
    p.setPen(QColor(CUR["accent"]))
    f = QFont()
    f.setBold(True)
    f.setPixelSize(72)
    p.setFont(f)
    p.drawText(QRect(52, 60, 152, 110), Qt.AlignCenter, "B")
    p.end()
    try:
        import os
        if not os.path.exists(os.path.join(DIR, "bebsi.ico")):
            pm.save(os.path.join(DIR, "bebsi.ico"))
    except Exception:
        pass
    try:
        _ic = QIcon(os.path.join(DIR, "bebsi.ico"))
        if not _ic.isNull():
            return _ic
    except Exception:
        pass
    return QIcon(pm)



# === EMOJI_STICKER_MENU ===
def _pkx_split(s):
    out = []
    for ch in s:
        if ch in "\ufe0f\u200d" and out:
            out[-1] += ch
        else:
            out.append(ch)
    return out
PKX_EMOJI = _pkx_split("😀😃😄😁😆😅😂🤣😊🙂😉😍🥰😘😙😚😋😛😝😜🤪🧐😎🥳😒😞😔😟😕🙁☹️😣😖😫😩🥺😭😤😠😡🤬😳🥵🥶😱😨😰😥🤗🤔🤭🤫🤥😶😐😑😬🙄😯😲😴🤤😵🥴🤢🤮🤧😷👎👌🤌✌️🤟🤘🙌👏🤝💪❤️💛💚💙💜🖤🤍💔️💕💞💓💗💖💘💝💯💢💥💫💦💨💬🔥✨🎉🎁⚽🎮🎯🎧🎵🎶🎬📸📌✂️🔒⭐⚡☀️🌙🌈🌊🍏🍊🍋🍉🍓🍑🍔🌭🧁☕🥂")
PKX_STICKERS = ["😂🔥", "🎉", "❤️", "💥", "✨", "👉👈", "💔😭", "✅👍", "🆗", "✨🌟",
                "💪🔥", "❤️", "😴💤", "🥐", "😋", "🎮", "️🌴", "❄️", "🌞🌻", "🐾",
                "🎧🎵", "️📝", "💯", "💰", "🌕", "✅", "❤️🔒", "😘", "🥳🎊", "🕶️"]

class PickDialogX(QDialog):
    def __init__(self, chat):
        super().__init__(chat)
        self.chat = chat
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setObjectName("dlg")
        self.setFixedWidth(404)
        v = QVBoxLayout(self)
        v.setContentsMargins(12, 12, 12, 12)
        v.setSpacing(8)
        head = QHBoxLayout()
        head.setSpacing(6)
        self.t_emo = QPushButton("😊  Эмодзи")
        self.t_stk = QPushButton("⭐  Стикеры")
        for b in (self.t_emo, self.t_stk):
            b.setCheckable(True)
            b.setCursor(Qt.PointingHandCursor)
            b.setFixedHeight(32)
            b.setStyleSheet(f"QPushButton{{background:{rgba(CUR['bubble'],220)};border:1px solid {rgba(CUR['stroke'],200)};border-radius:10px;padding:4px 16px;font-size:12px;font-weight:700;color:{CUR['muted']};}}QPushButton:checked{{background:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 {CUR['accent']},stop:1 {CUR['accent2']});color:#ffffff;border:none;}}")
        self.t_emo.setChecked(True)
        self.t_emo.clicked.connect(lambda: self._show(0))
        self.t_stk.clicked.connect(lambda: self._show(1))
        head.addWidget(self.t_emo)
        head.addWidget(self.t_stk)
        head.addStretch(1)
        cx = QPushButton("×")
        cx.setObjectName("closeBtn")
        cx.setFixedSize(26, 26)
        cx.clicked.connect(self.reject)
        head.addWidget(cx)
        v.addLayout(head)
        self.stack = QStackedWidget()
        self.stack.addWidget(self._grid(PKX_EMOJI, False))
        self.stack.addWidget(self._grid(PKX_STICKERS, True))
        v.addWidget(self.stack)
    def _grid(self, items, sticker):
        cell = 44 if not sticker else 64
        col = 8 if not sticker else 5
        fs = 21 if not sticker else 30
        sc = QScrollArea()
        sc.setWidgetResizable(False)
        sc.setFixedHeight(292)
        sc.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sc.setStyleSheet("QScrollArea{border:none;background:transparent;}")
        w = QWidget()
        w.setStyleSheet("background:transparent;")
        w.setFixedWidth(col * cell + 12)
        g = QGridLayout(w)
        g.setContentsMargins(6, 6, 6, 6)
        g.setSpacing(2)
        for i, it in enumerate(items):
            b = QPushButton(it)
            b.setFixedSize(cell - 2, cell - 2)
            b.setCursor(Qt.PointingHandCursor)
            b.setStyleSheet(f"QPushButton{{background:transparent;border:none;border-radius:10px;font-size:{fs}px;padding:0px;}}QPushButton:hover{{background:{rgba(CUR['hover'],220)};}}")
            if sticker:
                b.clicked.connect(lambda _, s=it: self._send_sticker(s))
            else:
                b.clicked.connect(lambda _, e=it: self._ins(e))
            g.addWidget(b, i // col, i % col)
        sc.setWidget(w)
        sc.setAlignment(Qt.AlignHCenter)
        return sc
    def _show(self, idx):
        self.stack.setCurrentIndex(idx)
        self.t_emo.setChecked(idx == 0)
        self.t_stk.setChecked(idx == 1)
    def _ins(self, e):
        try:
            self.chat.input.insert(e)
            self.chat.input.setFocus()
        except Exception:
            pass
    def _send_sticker(self, s):
        try:
            if self.chat.peer:
                self.chat.send_to(self.chat.peer, s)
        except Exception:
            pass
    def show_at(self):
        try:
            btn = getattr(self.chat, "emoji_btn", None)
            if btn is not None:
                p = btn.mapToGlobal(QPoint(0, 0))
                self.move(max(8, p.x() - 356), max(8, p.y() - 352))
        except Exception:
            pass
        fade_in(self, 150)
        self.exec()

def _pkx_open(self):
    PickDialogX(self).show_at()
ChatScreen.open_emoji = _pkx_open

if not getattr(MessageBubble._render_text, "_pkx", False):
    _pkx_rt = MessageBubble._render_text
    def _pkx_rt_w(self):
        _pkx_rt(self)
        try:
            t = (getattr(self, "_base", "") or "").strip()
            ok = "☕☀❤♥✅❌⭐\ufe0f\u200d"
            if 1 <= len(t) <= 4 and any(ord(c) >= 0x1F000 for c in t) and all(ord(c) >= 0x1F000 or c in ok for c in t):
                self.txt.setStyleSheet("font-size:52px;background:transparent;")
        except Exception:
            pass
    _pkx_rt_w._pkx = True
    MessageBubble._render_text = _pkx_rt_w

def main():
    try:
        import faulthandler as _fh
        _fh.enable(file=open(os.path.join(DIR, "faulthandler.log"), "a", buffering=1))
    except Exception:
        pass
    def _eh(t, v, tb):
        import traceback
        msg = "".join(traceback.format_exception(t, v, tb))
        print(msg)
        try:
            with open(os.path.join(DIR, "crash.log"), "a", encoding="utf-8") as f:
                f.write(msg + "\n")
        except Exception:
            pass
        try:
            if sys.stderr is not None:
                sys.__excepthook__(t, v, tb)
        except Exception:
            pass
    sys.excepthook = _eh
    load_settings()
    app = QApplication(sys.argv)
    try:
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Bebsi.App.1")
    except Exception:
        pass
    app.setWindowIcon(make_icon())
    app.setStyleSheet(build_qss(CUR) + "\n#inputWrap {background:" + CUR["bubble"] + "; border:1px solid " + CUR["stroke"] + "; border-radius:22px;}\n#inputWrap QLineEdit {background:transparent; border:none;}")
    pal = app.palette()
    pal.setColor(QPalette.PlaceholderText, QColor("#5d6579"))
    app.setPalette(pal)
    server_ok = ensure_server()
    w = Messenger(server_ok)
    QTimer.singleShot(800, w._auto_login)
    if LOCK_HASH:
        w.show_lock()
    w.setWindowTitle("")
    w.resize(1080, 680)
    w.setMinimumSize(880, 560)
    w.setWindowOpacity(0.0)
    w.show()
    try:
        pass
    except Exception:
        pass
    _fade = QPropertyAnimation(w, b"windowOpacity")
    _fade.setDuration(450)
    _fade.setStartValue(0.0)
    _fade.setEndValue(1.0)
    _fade.start()
    w._fade = _fade
    fade_in(w, 500)
    sys.exit(app.exec())


# === PICK_X1 ===
def _pkx_split(s):
    out = []
    for ch in s:
        if ch in "\ufe0f\u200d" and out:
            out[-1] += ch
        else:
            out.append(ch)
    return out
PKX_EMOJI = _pkx_split("😀😃😄😁😆😅😂🤣😊🙂😉😍🥰😘😙😚😋😛😝😜🤪🧐😎🥳😒😞😔😟😕🙁☹️😣😖😩🥺😭😤😠😡🤬😳🥵🥶😱😨😰😥🤗🤔🤭🤫🤥😶😐😑😬🙄😯😲😴🤤😵🥴🤢🤮🤧😷👎👌🤌✌️🤟🤘🙌👏🤝💪❤️💛💚💙💜🖤🤍💔️💕💞💓💗💖💘💝💯💢💥💫💦💨💬🔥✨🎉🎁⚽🎮🎯🎧🎵🎶🎬📸📌✂️🔒⭐⚡☀️🌙🌈🌊🍏🍊🍋🍉🍓🍑🍔🌭🧁☕🥂")
PKX_STICKERS = ["😂🔥", "🎉", "❤️", "💥", "✨", "👉👈", "💔😭", "✅👍", "🆗", "✨🌟",
                "💪🔥", "❤️", "😴💤", "🥐", "😋", "🎮", "️🌴", "❄️", "🌞🌻", "🐾",
                "🎧🎵", "️📝", "💯", "💰", "🌕", "✅", "❤️🔒", "😘", "🥳🎊", "🕶️"]
PKX_EFONT = 'font-family:"Segoe UI Emoji","Noto Color Emoji","Apple Color Emoji",sans-serif;'

class PickDialogX(QDialog):
    def __init__(self, chat):
        super().__init__(chat)
        self.chat = chat
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setObjectName("dlg")
        self.setFixedWidth(404)
        v = QVBoxLayout(self)
        v.setContentsMargins(12, 12, 12, 12)
        v.setSpacing(8)
        head = QHBoxLayout()
        head.setSpacing(6)
        self.t_emo = QPushButton("😊  Эмодзи")
        self.t_stk = QPushButton("⭐  Стикеры")
        for b in (self.t_emo, self.t_stk):
            b.setCheckable(True)
            b.setCursor(Qt.PointingHandCursor)
            b.setFixedHeight(32)
            b.setStyleSheet(f"QPushButton{{background:{rgba(CUR['bubble'],220)};border:1px solid {rgba(CUR['stroke'],200)};border-radius:10px;padding:4px 16px;font-size:12px;font-weight:700;color:{CUR['muted']};}}QPushButton:checked{{background:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 {CUR['accent']},stop:1 {CUR['accent2']});color:#ffffff;border:none;}}")
        self.t_emo.setChecked(True)
        self.t_emo.clicked.connect(lambda: self._show(0))
        self.t_stk.clicked.connect(lambda: self._show(1))
        head.addWidget(self.t_emo)
        head.addWidget(self.t_stk)
        head.addStretch(1)
        cx = QPushButton("×")
        cx.setObjectName("closeBtn")
        cx.setFixedSize(26, 26)
        cx.clicked.connect(self.reject)
        head.addWidget(cx)
        v.addLayout(head)
        self.stack = QStackedWidget()
        self.stack.addWidget(self._grid(PKX_EMOJI, False))
        self.stack.addWidget(self._grid(PKX_STICKERS, True))
        v.addWidget(self.stack)
    def _grid(self, items, sticker):
        cell = 44 if not sticker else 64
        col = 8 if not sticker else 5
        fs = 21 if not sticker else 30
        sc = QScrollArea()
        sc.setWidgetResizable(False)
        sc.setFixedHeight(292)
        sc.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sc.setStyleSheet("QScrollArea{border:none;background:transparent;}")
        w = QWidget()
        w.setStyleSheet("background:transparent;")
        w.setFixedWidth(col * cell + 12)
        g = QGridLayout(w)
        g.setContentsMargins(6, 6, 6, 6)
        g.setSpacing(2)
        for i, it in enumerate(items):
            b = QPushButton(it)
            b.setFixedSize(cell - 2, cell - 2)
            b.setCursor(Qt.PointingHandCursor)
            b.setStyleSheet(f"QPushButton{{background:transparent;border:none;border-radius:10px;font-size:{fs}px;padding:0px;{PKX_EFONT}}}QPushButton:hover{{background:{rgba(CUR['hover'],220)};}}")
            if sticker:
                b.clicked.connect(lambda _, s=it: self._send_sticker(s))
            else:
                b.clicked.connect(lambda _, e=it: self._ins(e))
            g.addWidget(b, i // col, i % col)
        sc.setWidget(w)
        sc.setAlignment(Qt.AlignHCenter)
        return sc
    def _show(self, idx):
        self.stack.setCurrentIndex(idx)
        self.t_emo.setChecked(idx == 0)
        self.t_stk.setChecked(idx == 1)
    def _ins(self, e):
        try:
            self.chat.input.insert(e)
            self.chat.input.setFocus()
        except Exception:
            pass
    def _send_sticker(self, s):
        try:
            if self.chat.peer:
                self.chat.send_to(self.chat.peer, s)
        except Exception:
            pass
    def show_at(self):
        try:
            btn = getattr(self.chat, "emoji_btn", None)
            if btn is None:
                for c in self.chat.findChildren(QPushButton):
                    if "emo" in (c.objectName() or "").lower():
                        btn = c
                        break
            if btn is not None:
                p = btn.mapToGlobal(QPoint(0, 0))
                self.move(max(8, p.x() - 356), max(8, p.y() - 352))
        except Exception:
            pass
        fade_in(self, 150)
        self.exec()

def _pkx_open(self):
    PickDialogX(self).show_at()
ChatScreen.open_emoji = _pkx_open

if not getattr(MessageBubble._render_text, "_pkx", False):
    _pkx_rt = MessageBubble._render_text
    def _pkx_rt_w(self):
        _pkx_rt(self)
        try:
            t = (getattr(self, "_base", "") or "").strip()
            ok = "☕☀❤♥✅❌⭐\ufe0f\u200d"
            if 1 <= len(t) <= 4 and any(ord(c) >= 0x1F000 for c in t) and all(ord(c) >= 0x1F000 or c in ok for c in t):
                self.txt.setStyleSheet(f"font-size:52px;background:transparent;{PKX_EFONT}")
        except Exception:
            pass
    _pkx_rt_w._pkx = True
    MessageBubble._render_text = _pkx_rt_w
# === PICK_FINAL + CMDS ===
def _pkf_split(s):
    out = []
    for ch in s:
        if ch in "\ufe0f\u200d" and out:
            out[-1] += ch
        else:
            out.append(ch)
    return out
PKF_EMOJI = _pkf_split("😀😃😄😁😆😅😂🤣😊🙂😉😍🥰😘😙😚😋😛😝😜🤪🧐😎🥳😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😤😠😡😳🥵🥶😱😨😰😥🤗🤔🤭🤫🤥😶😐😑😬🙄😯😲😴🤤😵🥴🤢🤮🤧😷👌🤌✌️🤟🤘🙌👏🤝💪❤️💛💚💙💜🖤🤍💔❣️💞💓💗💖💘💝💯💢💥💦💨💬🔥✨🎁🏀🎯🎵🎶🎬📸📌✂️🔒⭐☀️🌊🍏🍊🍋🍉🍓🍑🍔🌭🧁☕🥂")
PKF_STICKERS = ["😂🔥", "", "😍❤️", "🤯💥", "😎✨", "🥺👉👈", "💔😭", "✅👍", "🆗", "✨🌟",
                "💪🔥", "❤️", "😴💤", "🥐", "🍕", "🎮", "️🌴", "️⛄", "🌻", "🐾",
                "🎧🎵", "️📝", "💪", "💰", "🌕", "✅", "❤️", "👋😘", "🥳🎊", "🕶️"]

class PickDialogFinal(QDialog):
    def __init__(self, chat):
        super().__init__(chat)
        self.chat = chat
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setObjectName("dlg")
        self.setFixedWidth(404)
        v = QVBoxLayout(self)
        v.setContentsMargins(12, 12, 12, 12)
        v.setSpacing(8)
        head = QHBoxLayout()
        head.setSpacing(6)
        self.t_emo = QPushButton("😊  Эмодзи")
        self.t_stk = QPushButton("⭐  Стикеры")
        for b in (self.t_emo, self.t_stk):
            b.setCheckable(True)
            b.setCursor(Qt.PointingHandCursor)
            b.setFixedHeight(32)
            b.setStyleSheet(f"QPushButton{{background:{rgba(CUR['bubble'],220)};border:1px solid {rgba(CUR['stroke'],200)};border-radius:10px;padding:4px 16px;font-size:12px;font-weight:700;color:{CUR['text']};}}QPushButton:checked{{background:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 {CUR['accent']},stop:1 {CUR['accent2']});color:#ffffff;border:none;}}")
        self.t_emo.setChecked(True)
        self.t_emo.clicked.connect(lambda: self._show(0))
        self.t_stk.clicked.connect(lambda: self._show(1))
        head.addWidget(self.t_emo)
        head.addWidget(self.t_stk)
        head.addStretch(1)
        cx = QPushButton("×")
        cx.setObjectName("closeBtn")
        cx.setFixedSize(26, 26)
        cx.clicked.connect(self.reject)
        head.addWidget(cx)
        v.addLayout(head)
        self.stack = QStackedWidget()
        self.stack.addWidget(self._grid(PKF_EMOJI, False))
        self.stack.addWidget(self._grid(PKF_STICKERS, True))
        v.addWidget(self.stack)
    def _grid(self, items, sticker):
        cell = 44 if not sticker else 64
        col = 8 if not sticker else 5
        fs = 21 if not sticker else 30
        sc = QScrollArea()
        sc.setWidgetResizable(False)
        sc.setFixedHeight(292)
        sc.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sc.setStyleSheet("QScrollArea{border:none;background:transparent;}")
        w = QWidget()
        w.setStyleSheet("background:transparent;")
        w.setFixedWidth(col * cell + 12)
        g = QGridLayout(w)
        g.setContentsMargins(6, 6, 6, 6)
        g.setSpacing(2)
        for i, it in enumerate(items):
            b = QPushButton(it)
            b.setFixedSize(cell - 2, cell - 2)
            b.setCursor(Qt.PointingHandCursor)
            b.setStyleSheet(f"QPushButton{{background:transparent;border:none;border-radius:10px;font-size:{fs}px;padding:0px;}}QPushButton:hover{{background:{rgba(CUR['hover'],220)};}}")
            if sticker:
                b.clicked.connect(lambda _, s=it: self._send_sticker(s))
            else:
                b.clicked.connect(lambda _, e=it: self._ins(e))
            g.addWidget(b, i // col, i % col)
        sc.setWidget(w)
        sc.setAlignment(Qt.AlignHCenter)
        return sc
    def _show(self, idx):
        self.stack.setCurrentIndex(idx)
        self.t_emo.setChecked(idx == 0)
        self.t_stk.setChecked(idx == 1)
    def _ins(self, e):
        try:
            self.chat.input.insert(e)
            self.chat.input.setFocus()
        except Exception:
            pass
    def _send_sticker(self, s):
        try:
            if self.chat.peer:
                self.chat.send_to(self.chat.peer, s)
        except Exception:
            pass
    def show_at(self):
        try:
            btn = getattr(self.chat, "emoji_btn", None) or getattr(self.chat, "emo_btn", None)
            if btn is not None:
                p = btn.mapToGlobal(QPoint(0, 0))
                self.move(max(8, p.x() - 356), max(8, p.y() - 352))
        except Exception:
            pass
        fade_in(self, 150)
        self.exec()

def _pkf_open(self):
    PickDialogFinal(self).show_at()
ChatScreen.open_emoji = _pkf_open

if not getattr(MessageBubble._render_text, "_pkf", False):
    _pkf_rt = MessageBubble._render_text
    def _pkf_rt_w(self):
        _pkf_rt(self)
        try:
            t = (getattr(self, "_base", "") or "").strip()
            ok = "☕☀❤♥✅❌⭐\ufe0f\u200d"
            if 1 <= len(t) <= 4 and any(ord(c) >= 0x1F000 for c in t) and all(ord(c) >= 0x1F000 or c in ok for c in t):
                self.txt.setStyleSheet("font-size:52px;background:transparent;")
        except Exception:
            pass
    _pkf_rt_w._pkf = True
    MessageBubble._render_text = _pkf_rt_w

# ---------- слэш-команды ----------
if not getattr(ChatScreen.send_message, "_cmd", False):
    _cmd_sm = ChatScreen.send_message
    def _cmd_sm_w(self):
        t = self.input.text().strip()
        try:
            if t.startswith("/poll "):
                q = t[6:].strip()
                if q and self.peer:
                    self.input.clear()
                    dlg = PollDialog(self)
                    dlg.q.setText(q)
                    if dlg.exec() == QDialog.Accepted:
                        qq, opts = dlg.result_data()
                        if qq and len(opts) >= 2:
                            self.send_to(self.peer, poll=json.dumps({"question": qq, "options": opts, "votes": {}}, ensure_ascii=False), last="Опрос")
                    return
            if t.startswith("/remind ") and self.peer:
                m = re.match(r"/remind\s+(\d+)\s*([mhdмчд]?)\s+(.+)", t, re.I)
                if m:
                    n = int(m.group(1)); unit = (m.group(2) or "m").lower(); txt = m.group(3).strip()
                    from datetime import timedelta
                    if unit in ("h", "ч"):
                        dt = datetime.now() + timedelta(hours=n)
                    elif unit in ("d", "д"):
                        dt = datetime.now() + timedelta(days=n)
                    else:
                        dt = datetime.now() + timedelta(minutes=n)
                    SCHED.setdefault(self.me, []).append({"key": self.peer, "text": txt, "ts": dt.isoformat(timespec="seconds")})
                    save_extra()
                    self.input.clear()
                    self.show_warn("Напомню " + dt.strftime("%d.%m %H:%M") + " ⏰")
                    return
            if t == "/shrug":
                self.input.setText("¯\\_(ツ)_/¯")
        except Exception:
            pass
        _cmd_sm(self)
    _cmd_sm_w._cmd = True
    ChatScreen.send_message = _cmd_sm_w

# === WIN_ANIM_V1 ===
_INITN = chr(95) * 2 + "init" + chr(95) * 2

def _wa_geo(win, target, dur=200):
    try:
        a = QPropertyAnimation(win, b"geometry")
        a.setDuration(dur)
        a.setStartValue(win.geometry())
        a.setEndValue(target)
        a.setEasingCurve(QEasingCurve.OutCubic)
        win._wa_geo_anim = a
        a.start()
    except Exception:
        win.setGeometry(target)

def _wa_toggle_max(self):
    w = self.win
    try:
        scr = QApplication.primaryScreen().availableGeometry()
    except Exception:
        scr = None
    if scr is None:
        return
    if getattr(w, "_wa_maxed", False):
        tgt = getattr(w, "_wa_normal", None) or w.geometry()
        w._wa_maxed = False
        _wa_geo(w, tgt)
    else:
        w._wa_normal = w.geometry()
        w._wa_maxed = True
        _wa_geo(w, scr)

def _wa_anim_min(self):
    w = self.win
    if getattr(w, "_wa_min_busy", False):
        return
    w._wa_min_busy = True
    w._was_min = True
    a = QPropertyAnimation(w, b"windowOpacity")
    a.setDuration(150)
    a.setStartValue(w.windowOpacity())
    a.setEndValue(0.0)
    a.setEasingCurve(QEasingCurve.InCubic)
    def _fin():
        try:
            w.setWindowOpacity(1.0)
            w.showMinimized()
        finally:
            w._wa_min_busy = False
    a.finished.connect(_fin)
    w._wa_min_anim = a
    a.start()

def _wa_restore_pop(w):
    try:
        g = w.geometry()
        dw = int(g.width() * 0.05)
        dh = int(g.height() * 0.05)
        start = g.adjusted(dw, dh, -dw, -dh)
        w.setWindowOpacity(0.0)
        w.setGeometry(start)
        a1 = QPropertyAnimation(w, b"windowOpacity")
        a1.setDuration(220)
        a1.setStartValue(0.0)
        a1.setEndValue(1.0)
        a2 = QPropertyAnimation(w, b"geometry")
        a2.setDuration(220)
        a2.setStartValue(start)
        a2.setEndValue(g)
        a2.setEasingCurve(QEasingCurve.OutCubic)
        grp = QParallelAnimationGroup(w)
        grp.addAnimation(a1)
        grp.addAnimation(a2)
        w._wa_restore_grp = grp
        grp.start()
    except Exception:
        pass

def _wa_changeEvent(self, e):
    try:
        QStackedWidget.changeEvent(self, e)
    except Exception:
        pass
    try:
        if e.type() == QEvent.WindowStateChange:
            if not (self.windowState() & Qt.WindowMinimized) and getattr(self, "_was_min", False):
                self._was_min = False
                _wa_restore_pop(self)
    except Exception:
        pass

TitleBar.toggle_max = _wa_toggle_max
TitleBar.anim_min = _wa_anim_min
Messenger.changeEvent = _wa_changeEvent

_tb_init0 = getattr(TitleBar, _INITN)
def _tb_init_w(self, win):
    _tb_init0(self, win)
    try:
        self.min_b.clicked.disconnect()
    except Exception:
        pass
    self.min_b.clicked.connect(self.anim_min)
setattr(TitleBar, _INITN, _tb_init_w)

# === PICK_FINAL2 ===
def _pkf2_split(s):
    out = []
    for ch in s:
        if ch in "\ufe0f\u200d" and out:
            out[-1] += ch
        else:
            out.append(ch)
    return out
PKF2_EMOJI = _pkf2_split("😀😃😄😁😆😅😂🤣😊🙂😉😍🥰😘😙😚😋😛😝😜🤪🧐😎🥳😒😞😔😟😕🙁☹️😣😖😫😩🥺😢😤😠😡😳🥵🥶😱😨😰😥🤗🤔🤭🤫🤥😶😐😑😬🙄😯😲😴🤤😵🥴🤢🤮🤧😷👍👌🤌✌️🤟🤘🙌👏🤝💪❤️💛💚💙💜🖤🤍💔️💞💓💗💖💘💝💯💢💥💫💦💨💬🔥✨🎉🎁⚽🏀🎮🎯🎧🎵🎶🎬📸✂️⭐☀️🌊🍏🍊🍋🍉🍓🍑🍔🌭🧁☕🥂")
PKF2_STICKERS = ["😂🔥", "", "❤️", "🤯💥", "😎✨", "🥺👉👈", "💔😭", "✅👍", "🆗", "✨🌟",
                 "💪🔥", "🙏❤️", "😴💤", "☕🥐", "😋", "👾", "️🌴", "❄️⛄", "🌞🌻", "",
                 "🎧🎵", "✍️📝", "", "🤑💰", "🚀🌕", "✅", "❤️🔒", "👋😘", "🥳🎊", "️"]

class PickDialog2(QDialog):
    def __init__(self, chat):
        super().__init__(chat)
        self.chat = chat
        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setObjectName("dlg")
        self.setFixedWidth(404)
        v = QVBoxLayout(self)
        v.setContentsMargins(12, 12, 12, 12)
        v.setSpacing(8)
        head = QHBoxLayout()
        head.setSpacing(6)
        self.t_emo = QPushButton("😊  Эмодзи")
        self.t_stk = QPushButton("⭐  Стикеры")
        for b in (self.t_emo, self.t_stk):
            b.setCheckable(True)
            b.setCursor(Qt.PointingHandCursor)
            b.setFixedHeight(32)
            b.setStyleSheet(f"QPushButton{{background:{rgba(CUR['bubble'],220)};border:1px solid {rgba(CUR['stroke'],200)};border-radius:10px;padding:4px 16px;font-size:12px;font-weight:700;color:{CUR['text']};}}QPushButton:checked{{background:qlineargradient(x1:0,y1:0,x2:1,y2:1,stop:0 {CUR['accent']},stop:1 {CUR['accent2']});color:#ffffff;border:none;}}")
        self.t_emo.setChecked(True)
        self.t_emo.clicked.connect(lambda: self._show(0))
        self.t_stk.clicked.connect(lambda: self._show(1))
        head.addWidget(self.t_emo)
        head.addWidget(self.t_stk)
        head.addStretch(1)
        cx = QPushButton("×")
        cx.setObjectName("closeBtn")
        cx.setFixedSize(26, 26)
        cx.clicked.connect(self.reject)
        head.addWidget(cx)
        v.addLayout(head)
        self.stack = QStackedWidget()
        self.stack.addWidget(self._grid(PKF2_EMOJI, False))
        self.stack.addWidget(self._grid(PKF2_STICKERS, True))
        v.addWidget(self.stack)
    def _grid(self, items, sticker):
        cell = 44 if not sticker else 64
        col = 8 if not sticker else 5
        fs = 21 if not sticker else 30
        sc = QScrollArea()
        sc.setWidgetResizable(False)
        sc.setFixedHeight(292)
        sc.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sc.setStyleSheet("QScrollArea{border:none;background:transparent;}")
        w = QWidget()
        w.setStyleSheet("background:transparent;")
        w.setFixedWidth(col * cell + 12)
        g = QGridLayout(w)
        g.setContentsMargins(6, 6, 6, 6)
        g.setSpacing(2)
        for i, it in enumerate(items):
            b = QPushButton(it)
            b.setFixedSize(cell - 2, cell - 2)
            b.setCursor(Qt.PointingHandCursor)
            b.setStyleSheet(f"QPushButton{{background:transparent;border:none;border-radius:10px;font-size:{fs}px;padding:0px;}}QPushButton:hover{{background:{rgba(CUR['hover'],220)};}}")
            if sticker:
                b.clicked.connect(lambda _, s=it: self._send_sticker(s))
            else:
                b.clicked.connect(lambda _, e=it: self._ins(e))
            g.addWidget(b, i // col, i % col)
        sc.setWidget(w)
        sc.setAlignment(Qt.AlignHCenter)
        return sc
    def _show(self, idx):
        self.stack.setCurrentIndex(idx)
        self.t_emo.setChecked(idx == 0)
        self.t_stk.setChecked(idx == 1)
    def _ins(self, e):
        try:
            self.chat.input.insert(e)
            self.chat.input.setFocus()
        except Exception:
            pass
    def _send_sticker(self, s):
        try:
            if self.chat.peer:
                self.chat.send_to(self.chat.peer, s)
        except Exception:
            pass
    def show_at(self):
        try:
            btn = getattr(self.chat, "emoji_btn", None) or getattr(self.chat, "emo_btn", None)
            if btn is not None:
                p = btn.mapToGlobal(QPoint(0, 0))
                self.move(max(8, p.x() - 356), max(8, p.y() - 352))
        except Exception:
            pass
        fade_in(self, 150)
        self.exec()

def _pkf2_open(self):
    PickDialog2(self).show_at()
ChatScreen.open_emoji = _pkf2_open

if not getattr(MessageBubble._render_text, "_pkf2", False):
    _pkf2_rt = MessageBubble._render_text
    def _pkf2_rt_w(self):
        _pkf2_rt(self)
        try:
            t = (getattr(self, "_base", "") or "").strip()
            ok = "☕☀❤♥✅❌⭐\ufe0f\u200d"
            if 1 <= len(t) <= 4 and any(ord(c) >= 0x1F000 for c in t) and all(ord(c) >= 0x1F000 or c in ok for c in t):
                self.txt.setStyleSheet("font-size:52px;background:transparent;")
        except Exception:
            pass
    _pkf2_rt_w._pkf2 = True
    MessageBubble._render_text = _pkf2_rt_w

# === GUIDE_V2 ===
from PySide6.QtCore import QRect as _GRect, Property as _GProp
from PySide6.QtGui import QPainterPath as _GPath
GUIDE_PATH = os.path.join(DIR, "guide.json")
try:
    GUIDE_DONE = json.load(open(GUIDE_PATH, encoding="utf-8"))
except Exception:
    GUIDE_DONE = {}
def _save_guide():
    try:
        json.dump(GUIDE_DONE, open(GUIDE_PATH, "w", encoding="utf-8"))
    except Exception:
        pass
GUIDE_SLIDES = [
    ("👋 Добро пожаловать в Bebsi!",
     "Это твой личный мессенджер: чаты, звонки, истории и каналы.<br>За 30 секунд покажу, что тут есть и как создать аккаунт."),
    ("✨ Что умеет Bebsi",
     "• Голосовые с расшифровкой текста и видеокружки<br>• Истории на 24 часа и реакции на сообщения<br>• Группы, каналы и закрепы<br>• Отложенная отправка и напоминания<br>• Темы, обои и код-замок<br>• До трёх аккаунтов одновременно"),
    ("📝 Как создать аккаунт",
     "1. Нажми «Нет аккаунта? Создать»<br>2. Придумай уникальное имя пользователя<br>3. Пароль — минимум 6 символов<br>4. Почта необязательно: по ней можно войти кодом, если забудешь пароль<br>5. Жми «Создать аккаунт» — и ты внутри!"),
    ("🔑 Как входить потом",
     "Введи имя и пароль и нажми «Войти».<br>Забыл пароль? «✉️ Вход по почте» пришлёт код на привязанную почту.<br>Кнопка людей внизу слева переключает до 3 аккаунтов."),
    ("🎉 Готово!",
     "После входа я коротко подсвечу интерфейс: меню, поиск, чаты и кнопки.<br>Гайд сохранится и больше не появится."),
]

class WelcomeGuide(QWidget):
    def __init__(self, win):
        super().__init__(win)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.i = 0
        self.card = QFrame(self)
        self.card.setFixedWidth(400)
        self.card.setStyleSheet(f"QFrame{{background:{rgba(CUR['card'], 252)};border:1px solid {rgba(CUR['stroke'], 220)};border-radius:20px;}}")
        v = QVBoxLayout(self.card)
        v.setContentsMargins(22, 20, 22, 18)
        v.setSpacing(10)
        self.t = QLabel("")
        self.t.setStyleSheet(f"font-size:18px;font-weight:800;color:{CUR['text']};background:transparent;border:none;")
        self.t.setWordWrap(True)
        v.addWidget(self.t)
        self.x = QLabel("")
        self.x.setStyleSheet(f"font-size:13px;color:{CUR['muted']};background:transparent;border:none;")
        self.x.setWordWrap(True)
        v.addWidget(self.x)
        self.d = QLabel("")
        self.d.setStyleSheet(f"font-size:11px;color:{CUR['accent2']};background:transparent;border:none;letter-spacing:4px;")
        v.addWidget(self.d)
        row = QHBoxLayout()
        row.setSpacing(8)
        self.skip = QPushButton("Пропустить")
        self.skip.setObjectName("ghostBtn")
        self.skip.setCursor(Qt.PointingHandCursor)
        self.skip.clicked.connect(lambda: self.finish())
        row.addWidget(self.skip)
        row.addStretch(1)
        self.nx = QPushButton("Далее")
        self.nx.setObjectName("sendBtn")
        self.nx.setCursor(Qt.PointingHandCursor)
        self.nx.clicked.connect(self.next)
        row.addWidget(self.nx)
        bw = QWidget()
        bw.setStyleSheet("background:transparent;border:none;")
        bw.setLayout(row)
        v.addWidget(bw)
        self.card.hide()
    def show_guide(self):
        pw = self.parentWidget()
        if pw is None:
            return
        self.setGeometry(0, 0, pw.width(), pw.height())
        self.show()
        self.raise_()
        self._apply(0)
        self.card.show()
        try:
            fade_in(self.card, 250)
        except Exception:
            pass
    def _apply(self, i):
        self.i = i
        t, x = GUIDE_SLIDES[i]
        self.t.setText(t)
        self.x.setText(x)
        self.d.setText("● " * (i + 1) + "○ " * (len(GUIDE_SLIDES) - i - 1))
        self.nx.setText("Начать 🚀" if i == len(GUIDE_SLIDES) - 1 else "Далее")
        self.skip.setVisible(i < len(GUIDE_SLIDES) - 1)
        self._place()
    def _place(self):
        try:
            self.card.adjustSize()
        except Exception:
            pass
        cw, ch = self.card.width(), self.card.height()
        self.card.move(max(10, (self.width() - cw) // 2), max(10, (self.height() - ch) // 2))
    def next(self):
        if self.i + 1 >= len(GUIDE_SLIDES):
            self.finish()
        else:
            self._apply(self.i + 1)
    def finish(self):
        GUIDE_DONE["welcome"] = True
        _save_guide()
        self.hide()
        self.deleteLater()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.finish()
        else:
            super().keyPressEvent(e)
    def resizeEvent(self, e):
        super().resizeEvent(e)
        self._place()
    def paintEvent(self, e):
        p = QPainter(self)
        p.fillRect(self.rect(), QColor(0, 0, 0, 150))
        p.end()

def _show_welcome(win):
    try:
        if GUIDE_DONE.get("welcome"):
            return
        for w in win.findChildren(WelcomeGuide):
            return
        WelcomeGuide(win).show_guide()
    except Exception as ex:
        print("WELCOME ERR:", ex)

def _guide_list_widget(c):
    try:
        p = c.list_w.parent()
        while p is not None and not isinstance(p, QScrollArea):
            p = p.parent()
        return p or c.list_w
    except Exception:
        return None

class GuideOverlay(QWidget):
    def __init__(self, chat):
        super().__init__(chat.window())
        self.chat = chat
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.step = 0
        self._spot = _GRect(0, 0, 0, 0)
        self._has_spot = False
        c = chat
        self.steps = [
            (lambda: getattr(c, "menu_btn", None), "Меню ☰", "Профиль, контакты, новые группы и каналы, темы и блокировка — всё здесь."),
            (lambda: getattr(c, "search", None), "Поиск 🔍", "Начни печатать имя — найдёшь человека и откроешь чат."),
            (lambda: _guide_list_widget(c), "Чаты 💬", "Список переписок: папки, закрепы, непрочитанные и избранное."),
            (lambda: getattr(c, "input", None), "Сообщения ✍️", "Печатай тут. Смайлик — эмодзи и стикеры, скрепка — фото и файлы, Enter — отправить."),
            (lambda: getattr(c, "mic_btn", None), "Голос и кружки 🎤", "Микрофон — голосовое с расшифровкой, камера — видеокружок."),
            (lambda: getattr(c, "send_btn", None), "Отложенная отправка ⏰", "Зажми кнопку отправки — сообщение уйдёт само по расписанию."),
            (lambda: getattr(c, "me_avatar", None), "Профиль и истории 👤", "Клик по своей аватарке внизу — профиль, фото и «Моя история»."),
            (lambda: None, "Реакции и меню сообщения", "Двойной клик по пузырю — реакции, правый клик — ответить, цитировать, переслать, закрепить, удалить."),
        ]
        self.card = QFrame(self)
        self.card.setFixedWidth(340)
        self.card.setStyleSheet(f"QFrame{{background:{rgba(CUR['card'], 250)};border:1px solid {rgba(CUR['stroke'], 220)};border-radius:16px;}}")
        v = QVBoxLayout(self.card)
        v.setContentsMargins(16, 14, 16, 14)
        v.setSpacing(8)
        self.t_lbl = QLabel("")
        self.t_lbl.setStyleSheet(f"font-size:16px;font-weight:800;color:{CUR['text']};background:transparent;border:none;")
        self.t_lbl.setWordWrap(True)
        v.addWidget(self.t_lbl)
        self.x_lbl = QLabel("")
        self.x_lbl.setStyleSheet(f"font-size:13px;color:{CUR['muted']};background:transparent;border:none;")
        self.x_lbl.setWordWrap(True)
        v.addWidget(self.x_lbl)
        self.d_lbl = QLabel("")
        self.d_lbl.setStyleSheet(f"font-size:12px;color:{CUR['accent2']};background:transparent;border:none;letter-spacing:3px;")
        v.addWidget(self.d_lbl)
        row = QHBoxLayout()
        row.setSpacing(8)
        self.skip_b = QPushButton("Пропустить")
        self.skip_b.setObjectName("ghostBtn")
        self.skip_b.setCursor(Qt.PointingHandCursor)
        self.skip_b.clicked.connect(lambda: self.finish(False))
        row.addWidget(self.skip_b)
        row.addStretch(1)
        self.next_b = QPushButton("Далее")
        self.next_b.setObjectName("sendBtn")
        self.next_b.setCursor(Qt.PointingHandCursor)
        self.next_b.clicked.connect(self.next)
        row.addWidget(self.next_b)
        bw = QWidget()
        bw.setStyleSheet("background:transparent;border:none;")
        bw.setLayout(row)
        v.addWidget(bw)
        self.card.hide()
    def _get_spot(self):
        return self._spot
    def _set_spot(self, r):
        self._spot = r
        self._place_card()
        self.update()
    spotRect = _GProp(_GRect, _get_spot, _set_spot)
    def show_guide(self):
        pw = self.parentWidget()
        if pw is None:
            return
        self.setGeometry(0, 0, pw.width(), pw.height())
        self.show()
        self.raise_()
        self._apply(0)
        self.card.show()
        try:
            fade_in(self.card, 250)
        except Exception:
            pass
    def _apply(self, i):
        self.step = i
        get, title, text = self.steps[i]
        w = None
        try:
            w = get()
        except Exception:
            w = None
        self._has_spot = w is not None and w.isVisible()
        if self._has_spot:
            g = w.mapToGlobal(QPoint(0, 0))
            tl = self.mapFromGlobal(g)
            tgt = _GRect(tl.x() - 5, tl.y() - 5, w.width() + 10, w.height() + 10)
        else:
            pr = self.rect()
            tgt = _GRect(pr.center().x() - 150, pr.center().y() - 160, 300, 300)
        self.t_lbl.setText(title)
        self.x_lbl.setText(text)
        self.d_lbl.setText("● " * (i + 1) + "○ " * (len(self.steps) - i - 1))
        self.next_b.setText("Готово 🎉" if i == len(self.steps) - 1 else "Далее")
        a = QPropertyAnimation(self, b"spotRect")
        a.setDuration(280)
        a.setStartValue(self._spot if self._spot.width() > 0 else tgt)
        a.setEndValue(tgt)
        a.setEasingCurve(QEasingCurve.OutCubic)
        self._sa = a
        a.start()
        self._place_card(tgt)
    def _place_card(self, tgt=None):
        r = tgt or self._spot
        try:
            self.card.adjustSize()
        except Exception:
            pass
        ch = self.card.height() or 150
        y = r.bottom() + 14
        if y + ch > self.height() - 10:
            y = max(10, r.top() - ch - 14)
        x = min(max(10, r.center().x() - 170), max(10, self.width() - 350))
        self.card.move(x, y)
    def next(self):
        if self.step + 1 >= len(self.steps):
            self.finish(True)
        else:
            self._apply(self.step + 1)
    def finish(self, ok):
        try:
            name = getattr(self.chat, "me", None)
            if name:
                GUIDE_DONE[name] = True
                _save_guide()
            if ok:
                self.chat.show_warn("Гайд пройден! Всё твоё — пользуйся 🎉")
        except Exception:
            pass
        self.hide()
        self.deleteLater()
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.finish(False)
        else:
            super().keyPressEvent(e)
    def resizeEvent(self, e):
        super().resizeEvent(e)
        try:
            self._apply(self.step)
        except Exception:
            pass
    def paintEvent(self, e):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        path = _GPath()
        path.addRect(0, 0, self.width(), self.height())
        if self._has_spot and self._spot.width() > 0:
            path.addRoundedRect(float(self._spot.x()), float(self._spot.y()), float(self._spot.width()), float(self._spot.height()), 14, 14)
        p.setBrush(QColor(0, 0, 0, 165))
        p.setPen(Qt.NoPen)
        p.drawPath(path)
        if self._has_spot and self._spot.width() > 0:
            pen = QPen(QColor(CUR["accent2"]))
            pen.setWidth(2)
            p.setPen(pen)
            p.setBrush(Qt.NoBrush)
            p.drawRoundedRect(self._spot, 14, 14)
        p.end()

def _start_tour(chat):
    try:
        for ch in chat.window().findChildren(GuideOverlay):
            return
        GuideOverlay(chat).show_guide()
    except Exception as ex:
        print("TOUR ERR:", ex)

if not getattr(Messenger.__init__, "_wg", False):
    _wg_init = Messenger.__init__
    def _wg_init_w(self, *a, **kw):
        _wg_init(self, *a, **kw)
        try:
            QTimer.singleShot(900, lambda: _show_welcome(self))
        except Exception:
            pass
    _wg_init_w._wg = True
    Messenger.__init__ = _wg_init_w

if not getattr(ChatScreen.set_me, "_gt", False):
    _gt_sm = ChatScreen.set_me
    def _gt_sm_w(self, name, profile):
        _gt_sm(self, name, profile)
        try:
            if not GUIDE_DONE.get(name):
                QTimer.singleShot(1500, lambda: _start_tour(self))
        except Exception:
            pass
    _gt_sm_w._gt = True
    ChatScreen.set_me = _gt_sm_w

# === PACK2 ===
from datetime import timedelta
from PySide6.QtWidgets import QSpinBox
try:
    import winreg as _wr
except Exception:
    _wr = None
ARCH = set(_ex.get("arch", []))
SNOOZE = _ex.get("snooze", {})
NIGHT = _ex.get("night", [False, 23, 7])
SOUND_PACK = _ex.get("sound_pack", "pop")
UI_ZOOM = int(_ex.get("ui_zoom", 100))
SEL_MIDS = set()
if UI_ZOOM != 100:
    os.environ.setdefault("QT_SCALE_FACTOR", str(UI_ZOOM / 100.0))
def _save_pack2():
    try:
        try:
            d = json.load(open(EXTRA_PATH, encoding="utf-8"))
        except Exception:
            d = {}
        d["arch"] = list(ARCH)
        d["snooze"] = SNOOZE
        d["night"] = NIGHT
        d["sound_pack"] = SOUND_PACK
        d["ui_zoom"] = UI_ZOOM
        json.dump(d, open(EXTRA_PATH, "w", encoding="utf-8"))
    except Exception:
        pass
def night_active():
    if not NIGHT[0]:
        return False
    h = datetime.now().hour
    f, t = NIGHT[1], NIGHT[2]
    return f <= h < t if f <= t else (h >= f or h < t)
_orig_pop_wav = make_pop_wav
def make_pop_wav():
    kind = SOUND_PACK
    if kind == "pop":
        return _orig_pop_wav()
    path = os.path.join(tempfile.gettempdir(), "bebsi_" + kind + ".wav")
    if os.path.exists(path):
        return path
    import wave as _w, io as _io, math as _m
    sr = 22050
    buf = _io.BytesIO()
    w = _w.open(buf, "wb")
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    if kind == "ping":
        nn = int(sr * 0.25)
        for i in range(nn):
            t = i / sr
            env = (1 - i / nn) ** 1.5
            v = int(11000 * env * _m.sin(2 * _m.pi * 880 * t) + 5000 * env * _m.sin(2 * _m.pi * 1320 * t))
            w.writeframes(v.to_bytes(2, "little", signed=True))
    else:
        nn = int(sr * 0.22)
        for i in range(nn):
            t = i / sr
            env = (1 - i / nn) ** 2
            fq = 300 + 900 * (i / nn)
            v = int(12000 * env * _m.sin(2 * _m.pi * fq * t))
            w.writeframes(v.to_bytes(2, "little", signed=True))
    w.close()
    with open(path, "wb") as f:
        f.write(buf.getvalue())
    return path
def _autostart_cmd():
    if getattr(sys, "frozen", False):
        return '"' + os.path.abspath(sys.executable) + '"'
    exe = sys.executable.replace("python.exe", "pythonw.exe")
    if not os.path.exists(exe):
        exe = sys.executable
    return '"' + exe + '" "' + CLIENT_PATH + '"'
def autostart_on():
    if _wr is None:
        return False
    try:
        k = _wr.OpenKey(_wr.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
        try:
            v = _wr.QueryValueEx(k, "Bebsi")[0]
        except OSError:
            v = None
        _wr.CloseKey(k)
        return bool(v)
    except Exception:
        return False
def set_autostart(on):
    if _wr is None:
        return False
    try:
        k = _wr.OpenKey(_wr.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, _wr.KEY_SET_VALUE)
        if on:
            _wr.SetValueEx(k, "Bebsi", 0, _wr.REG_SZ, _autostart_cmd())
        else:
            try:
                _wr.DeleteValue(k, "Bebsi")
            except OSError:
                pass
        _wr.CloseKey(k)
        return True
    except Exception:
        return False
_bq0 = build_qss
def build_qss(t):
    return _bq0(t) + f'\n#bubbleMine[sel="true"], #bubbleOther[sel="true"] {{ border: 2px solid {t["accent2"]}; }}\n'
def global_search(self):
    d = QDialog(self)
    d.setWindowTitle("Поиск по всем чатам")
    d.resize(460, 420)
    v = QVBoxLayout(d)
    ed = QLineEdit()
    ed.setPlaceholderText("Найти во всех чатах…")
    lst = QListWidget()
    v.addWidget(ed)
    v.addWidget(lst, 1)
    hits = []
    def run():
        q = ed.text().strip().lower()
        lst.clear()
        hits.clear()
        if len(q) < 2:
            return
        for key, msgs in self.cache.items():
            disp = self.chats.get(key, {}).get("display", key)
            for m in msgs[-200:]:
                if q in (m.get("text") or "").lower():
                    hits.append((key, m))
                    lst.addItem(f"{disp} · {(m.get('ts') or '')[11:16]} — {(m.get('text') or '')[:60]}")
        if not hits:
            lst.addItem("Ничего не найдено")
    ed.textChanged.connect(lambda: run())
    def go(i):
        if 0 <= i < len(hits):
            key, m = hits[i]
            d.accept()
            self.open_chat(key)
            mid = m.get("id")
            if mid:
                QTimer.singleShot(400, lambda: self._jump_mid(mid))
    lst.itemActivated.connect(lambda it: go(lst.row(it)))
    lst.itemClicked.connect(lambda it: go(lst.row(it)))
    run()
    d.exec()
def _jump_mid(self, mid):
    b = self.bubbles_by_id.get(mid)
    if b is not None:
        self.scroll.ensureWidgetVisible(b, 60, 60)
        fade_in(b, 250)
def open_night_dialog(self):
    d = QDialog(self)
    d.setWindowTitle("Ночной режим")
    d.setFixedWidth(320)
    v = QVBoxLayout(d)
    cb = QCheckBox("Включать тёмную тему по расписанию")
    cb.setChecked(bool(NIGHT[0]))
    v.addWidget(cb)
    r = QHBoxLayout()
    r.addWidget(QLabel("с"))
    sf = QSpinBox(); sf.setRange(0, 23); sf.setValue(NIGHT[1])
    r.addWidget(sf)
    r.addWidget(QLabel("до"))
    st = QSpinBox(); st.setRange(0, 23); st.setValue(NIGHT[2])
    r.addWidget(st)
    rw = QWidget(); rw.setLayout(r)
    v.addWidget(rw)
    ok = QPushButton("Сохранить")
    ok.setObjectName("sendBtn")
    ok.clicked.connect(d.accept)
    v.addWidget(ok)
    if d.exec() == QDialog.Accepted:
        NIGHT[0] = cb.isChecked(); NIGHT[1] = sf.value(); NIGHT[2] = st.value()
        _save_pack2()
        try:
            self.app._night_state = None
        except Exception:
            pass
        self.show_warn("Ночной режим сохранён 🌙")
def toggle_autostart(self):
    on = autostart_on()
    ok = set_autostart(not on)
    self.show_warn(("Автозапуск включён 🚀" if not on else "Автозапуск выключен") if ok else "Не удалось изменить реестр")
def cycle_sound(self):
    global SOUND_PACK
    packs = ["pop", "ping", "bubble"]
    SOUND_PACK = packs[(packs.index(SOUND_PACK) + 1) % len(packs)] if SOUND_PACK in packs else "pop"
    _save_pack2()
    try:
        self.app.pop.setSource(QUrl.fromLocalFile(make_pop_wav()))
        self.app.pop.play()
    except Exception:
        pass
    self.show_warn("Звук уведомления: " + SOUND_PACK + " 🔊")
def set_ui_zoom(self):
    global UI_ZOOM
    v, ok = QInputDialog.getInt(self, "Масштаб интерфейса", "Процент (100 = обычно):", UI_ZOOM, 75, 200, 5)
    if not ok or v == UI_ZOOM:
        return
    UI_ZOOM = v
    _save_pack2()
    os.environ["QT_SCALE_FACTOR"] = str(v / 100.0)
    self.show_warn("Масштаб сохранён — перезапускаюсь…")
    def _rs():
        try:
            if getattr(sys, "frozen", False):
                _do_self_restart()
            else:
                subprocess.Popen([sys.executable, CLIENT_PATH], cwd=DIR)
        except Exception:
            pass
        os._exit(0)
    QTimer.singleShot(900, _rs)
ChatScreen.global_search = global_search
ChatScreen._jump_mid = _jump_mid
ChatScreen.open_night_dialog = open_night_dialog
ChatScreen.toggle_autostart = toggle_autostart
ChatScreen.cycle_sound = cycle_sound
ChatScreen.set_ui_zoom = set_ui_zoom
_ro0 = ChatScreen.refresh_order
def _ro2(self):
    _ro0(self)
    try:
        fol = getattr(self, "folder", "all")
        now = datetime.now().isoformat(timespec="seconds")
        for n, it in self.items.items():
            if n == "saved":
                continue
            arch = n in ARCH
            snz = SNOOZE.get(n) or ""
            snoozed = bool(snz) and snz > now
            if fol == "arch":
                it.setVisible(bool(arch and not snoozed))
            elif arch or snoozed:
                it.setVisible(False)
    except Exception:
        pass
ChatScreen.refresh_order = _ro2
_kp0 = ChatScreen.keyPressEvent
def _kp2(self, e):
    mod = e.modifiers()
    if mod & Qt.ControlModifier and mod & Qt.ShiftModifier and e.key() == Qt.Key_F:
        self.global_search()
        return
    if mod & Qt.ControlModifier and Qt.Key_1 <= e.key() <= Qt.Key_5:
        self.set_folder(["all", "personal", "groups", "unread", "arch"][e.key() - Qt.Key_1])
        return
    _kp0(self, e)
ChatScreen.keyPressEvent = _kp2
_cs_init0 = ChatScreen.__init__
def _cs_init2(self, app):
    _cs_init0(self, app)
    try:
        fb = QPushButton("🗄 Архив")
        fb.setObjectName("chipBtn")
        fb.setCursor(Qt.PointingHandCursor)
        fb.setProperty("mine", "false")
        fb.clicked.connect(lambda _, f="arch": self.set_folder(f))
        self.folder_bar.insertWidget(self.folder_bar.count() - 1, fb)
        self._folder_btns["arch"] = fb
    except Exception:
        pass
    try:
        lay = self.drawer.layout()
        for ic, lb, fn in (("🔎", "Поиск по всем чатам", self.global_search),
                           ("🌙", "Ночной режим", self.open_night_dialog),
                           ("🚀", "Автозапуск вкл/выкл", self.toggle_autostart),
                           ("🔊", "Звук уведомления", self.cycle_sound),
                           ("🔍", "Масштаб интерфейса", self.set_ui_zoom)):
            b = QPushButton(f"{ic}  {lb}")
            b.setCursor(Qt.PointingHandCursor)
            b.setStyleSheet(f"background: {rgba(CUR['hover'], 170)}; border-radius: 12px; padding: 10px 12px; text-align: left; font-size: 14px; font-weight: 600; border: none; color: {CUR['text']};")
            b.clicked.connect(lambda _, f=fn: (self.close_drawer(), f()))
            lay.insertWidget(lay.count() - 1, b)
    except Exception:
        pass
ChatScreen.__init__ = _cs_init2
_ms_init0 = Messenger.__init__
def _ms_init2(self, server_ok=True):
    _ms_init0(self, server_ok)
    try:
        self._really_close = False
        self._night_state = None
        self._tray_ctx_ts = 0.0
        m = QMenu(self)
        a_open = m.addAction("Открыть окно")
        m.addSeparator()
        a_quit = m.addAction("✖ Закрыть приложение")
        a_open.triggered.connect(self._tray_show)
        a_quit.triggered.connect(self._tray_quit)
        self.tray.setContextMenu(m)
        self.tray.activated.connect(self._tray_act)
        self._night_t = QTimer(self)
        self._night_t.setInterval(60000)
        self._night_t.timeout.connect(self._night_tick)
        self._night_t.start()
    except Exception as ex:
        print("TRAY INIT ERR:", ex)
def _tray_show(self):
    try:
        st = self.windowState()
        if st & Qt.WindowMinimized:
            st &= ~Qt.WindowMinimized
            self.setWindowState(st or Qt.WindowNoState)
        self.show()
        self.raise_()
        self.activateWindow()
    except Exception:
        pass
def _tray_act(self, reason):
    import time as _t
    now = _t.time()
    if reason == QSystemTrayIcon.Context:
        self._tray_ctx_ts = now
        return
    if reason != QSystemTrayIcon.Trigger and reason != QSystemTrayIcon.DoubleClick:
        return
    if now - getattr(self, "_tray_ctx_ts", 0.0) < 0.7:
        return
    if self.isVisible() and not self.isMinimized() and self.isActiveWindow():
        self.hide()
    else:
        self._tray_show()
def _tray_quit(self):
    self._really_close = True
    try:
        save_settings()
    except Exception:
        pass
    try:
        _save_disk_cache(self.chat)
    except Exception:
        pass
    try:
        if self.net:
            self.net.close()
    except Exception:
        pass
    QApplication.quit()
    import threading as _th
    _th.Timer(3.0, lambda: os._exit(0)).start()
_ms_ce0 = Messenger.closeEvent
def _ms_ce2(self, e):
    if getattr(self, "_really_close", False):
        _ms_ce0(self, e)
        return
    e.ignore()
    try:
        save_settings()
        _save_disk_cache(self.chat)
    except Exception:
        pass
    self.hide()
    try:
        self.tray.showMessage("Bebsi", "Я в трее — клик по иконке вернёт окно", self.tray.icon(), 1500)
    except Exception:
        pass
Messenger.__init__ = _ms_init2
Messenger._tray_show = _tray_show
Messenger._tray_act = _tray_act
Messenger._tray_quit = _tray_quit
Messenger.closeEvent = _ms_ce2

# === CACHE_FIX_V1 ===
def _cache_path(me):
    return os.path.join(DIR, "cache_" + str(me) + ".json")
def _load_disk_cache(chat):
    try:
        p = _cache_path(chat.me)
        if not os.path.exists(p):
            return
        d = json.load(open(p, encoding="utf-8"))
        for k, v in (d or {}).items():
            if isinstance(v, list) and v:
                merged = {}
                for m in v:
                    if isinstance(m, dict):
                        merged[(m.get("ts"), m.get("text"), bool(m.get("mine")))] = m
                for m in (chat.cache.get(k) or []):
                    merged[(m.get("ts"), m.get("text"), bool(m.get("mine")))] = m
                chat.cache[k] = sorted(merged.values(), key=lambda m: m.get("ts") or "")[-300:]
        for k in list(chat.cache):
            try:
                chat.update_preview(k, chat.cache[k])
            except Exception:
                pass
    except Exception as ex:
        print("CACHE LOAD ERR:", ex)
def _save_disk_cache(chat):
    try:
        if not getattr(chat, "me", None):
            return
        out = {}
        for k, msgs in chat.cache.items():
            slim = []
            for m in (msgs or [])[-200:]:
                mm = dict(m)
                for f in ("media", "voice", "video", "file_data"):
                    if len(mm.get(f) or "") > 400000:
                        mm[f] = ""
                slim.append(mm)
            out[k] = slim
        tmp = _cache_path(chat.me) + ".tmp"
        json.dump(out, open(tmp, "w", encoding="utf-8"), ensure_ascii=False)
        os.replace(tmp, _cache_path(chat.me))
    except Exception as ex:
        print("CACHE SAVE ERR:", ex)
_sm0c = ChatScreen.set_me
def _sm_cache(self, name, profile):
    _sm0c(self, name, profile)
    try:
        _load_disk_cache(self)
        if getattr(self, "_cache_t", None) is None:
            self._cache_t = QTimer(self)
            self._cache_t.setInterval(5000)
            self._cache_t.timeout.connect(lambda: _save_disk_cache(self))
            self._cache_t.start()
    except Exception:
        pass
ChatScreen.set_me = _sm_cache
_mc0c = Messenger.closeEvent
def _mc_cache(self, e):
    try:
        _save_disk_cache(self.chat)
    except Exception:
        pass
    _mc0c(self, e)
Messenger.closeEvent = _mc_cache
_hh0c = ChatScreen.handle_history
def _hh_dbg(self, peer, messages):
    try:
        if not messages:
            with open(os.path.join(DIR, "history_debug.log"), "a", encoding="utf-8") as f:
                f.write(time.strftime("%H:%M:%S") + " peer=" + str(peer) + " EMPTY\n")
    except Exception:
        pass
    _hh0c(self, peer, messages)
ChatScreen.handle_history = _hh_dbg

# === TRAY_FIX_V1 ===
def _tf_restore(win):
    try:
        win.setWindowOpacity(1.0)
        if win.isMinimized():
            win.showNormal()
        else:
            win.show()
        win.raise_()
        win.activateWindow()
        try:
            import ctypes
            ctypes.windll.user32.SetForegroundWindow(int(win.winId()))
        except Exception:
            pass
    except Exception:
        pass
_tf_init0 = Messenger.__init__
def _tf_init(self, server_ok=True):
    _tf_init0(self, server_ok)
    try:
        self._really_close = False
        m = QMenu(self)
        a_open = m.addAction("Открыть")
        a_quit = m.addAction("Выйти")
        a_open.triggered.connect(lambda: _tf_restore(self))
        a_quit.triggered.connect(self._tf_quit)
        self.tray.setContextMenu(m)
        try:
            self.tray.activated.disconnect()
        except Exception:
            pass
        self.tray.activated.connect(self._tf_act)
    except Exception:
        pass
def _tf_act(self, reason):
    try:
        if self.isVisible() and not self.isMinimized() and self.isActiveWindow():
            self.hide()
        else:
            _tf_restore(self)
    except Exception:
        pass
def _tf_quit(self):
    self._really_close = True
    try:
        save_settings()
    except Exception:
        pass
    try:
        _save_disk_cache(self.chat)
    except Exception:
        pass
    try:
        if self.net:
            self.net.close()
    except Exception:
        pass
    QApplication.quit()
    import threading as _th
    _th.Timer(3.0, lambda: os._exit(0)).start()
Messenger.__init__ = _tf_init
Messenger._tf_act = _tf_act
Messenger._tf_quit = _tf_quit
_tf_ce0 = Messenger.closeEvent
def _tf_ce(self, e):
    if getattr(self, "_really_close", False):
        try:
            save_settings()
        except Exception:
            pass
        try:
            _save_disk_cache(self.chat)
        except Exception:
            pass
        _tf_ce0(self, e)
    else:
        e.ignore()
        try:
            save_settings()
        except Exception:
            pass
        try:
            _save_disk_cache(self.chat)
        except Exception:
            pass
        self.hide()
        try:
            self.tray.showMessage(APP_NAME, "Я в трее — клик по иконке вернёт окно", self.tray.icon(), 1500)
        except Exception:
            pass
Messenger.closeEvent = _tf_ce
_tf_ch0 = Messenger.changeEvent
def _tf_ch(self, e):
    _tf_ch0(self, e)
    try:
        if e.type() == QEvent.WindowStateChange:
            if not (self.windowState() & Qt.WindowMinimized):
                QTimer.singleShot(0, self._tf_focus)
    except Exception:
        pass
def _tf_focus(self):
    try:
        self.raise_()
        self.activateWindow()
    except Exception:
        pass
Messenger.changeEvent = _tf_ch
Messenger._tf_focus = _tf_focus


# === REPAIR_V1 ===
# import shutil as _shu
# try:
#     if not SETTINGS.get("accounts") and os.path.exists(SETTINGS_PATH + ".bak"):
#         _bak = json.load(open(SETTINGS_PATH + ".bak", encoding="utf-8"))
#         if _bak.get("accounts"):
#             SETTINGS.clear()
#             SETTINGS.update(_bak)
#             save_settings()
#             print("SETTINGS HEALED from .bak")
# except Exception as _he:
#     print("HEAL ERR:", _he)
# _ss0r = save_settings
# def save_settings():
#     try:
#         if os.path.exists(SETTINGS_PATH):
#             _shu.copyfile(SETTINGS_PATH, SETTINGS_PATH + ".bak")
#     except Exception:
#         pass
#     _ss0r()

# === ACC_FIX_V1 ===
_PENDING_PW = {}
def _acc_path():
    return os.path.join(DIR, "accounts.json")
def _acc_load():
    try:
        return json.load(open(_acc_path(), encoding="utf-8")) or {}
    except Exception:
        return {}
def _acc_save(d):
    try:
        tmp = _acc_path() + ".tmp"
        json.dump(d, open(tmp, "w", encoding="utf-8"))
        os.replace(tmp, _acc_path())
    except Exception:
        pass
def _enc_pw(pw):
    try:
        import win32crypt
        return base64.b64encode(win32crypt.CryptProtectData(pw.encode("utf-8"), "bebsi", None, None, None, 0)).decode()
    except Exception:
        return ""
def _dec_pw(blob):
    try:
        import win32crypt
        return win32crypt.CryptUnprotectData(base64.b64decode(blob), None, None, None, None, 0)[1].decode("utf-8")
    except Exception:
        return ""
_ds0a = AuthScreen.do_submit
def _ds_acc(self):
    try:
        u = self.u.text().strip()
        p = self.p.text()
        if u and p:
            _PENDING_PW[u] = p
    except Exception:
        pass
    _ds0a(self)
AuthScreen.do_submit = _ds_acc
_sm0a = ChatScreen.set_me
def _sm_acc(self, name, profile):
    _sm0a(self, name, profile)
    try:
        pw = _PENDING_PW.get(name) or ""
        d = _acc_load()
        if pw:
            blob = _enc_pw(pw)
            if blob:
                d[name] = {"pw": blob, "last": time.time()}
                _acc_save(d)
        elif name in d:
            d[name]["last"] = time.time()
            _acc_save(d)
    except Exception:
        pass
ChatScreen.set_me = _sm_acc
_se0a = AuthScreen.showEvent
def _se_acc(self, e):
    _se0a(self, e)
    if getattr(self, "_acc_tried", False):
        return
    self._acc_tried = True
    d = _acc_load()
    if not d:
        return
    name = max(d.keys(), key=lambda k: d[k].get("last", 0))
    pw = _dec_pw(d[name].get("pw", ""))
    if not pw:
        return
    try:
        self.u.setText(name)
        self.p.setText(pw)
    except Exception:
        pass
    def _try(n=0):
        try:
            app = self.window()
            if getattr(app, "authed", False) or not self.isVisible():
                return
            net = getattr(app, "net", None)
            ok = net is not None and getattr(net, "sock", None) is not None or (net is not None and getattr(net, "connected", False))
            if ok:
                _PENDING_PW[name] = pw
                self.submit.emit(getattr(self, "mode", None) or "login", name, pw)
                return
        except Exception:
            pass
        if n < 12:
            QTimer.singleShot(700, lambda: _try(n + 1))
    QTimer.singleShot(1000, lambda: _try(0))
AuthScreen.showEvent = _se_acc


# === TRAY_SAVE_FIX_V4 ===
# Гарантированное сохранение настроек и аккаунтов при сворачивании в трей и выходе
def _safe_tray_close(self, e):
    if getattr(self, "_really_close", False):
        try:
            save_settings()
            if hasattr(self, 'chat') and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        e.accept()
    else:
        e.ignore()
        try:
            save_settings()
            if hasattr(self, 'chat') and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        self.hide()
        try:
            self.tray.showMessage("Bebsi", "Приложение свёрнуто в трей", self.tray.icon(), 1500)
        except Exception:
            pass

def _safe_tray_quit(self):
    self._really_close = True
    try:
        save_settings()
        if hasattr(self, 'chat') and self.chat:
            _save_disk_cache(self.chat)
    except Exception:
        pass
    try:
        if getattr(self, 'net', None):
            self.net.close()
    except Exception:
        pass
    from PySide6.QtWidgets import QApplication
    QApplication.quit()

# Перекрываем предыдущие патчи трея
Messenger.closeEvent = _safe_tray_close
Messenger._tf_quit = _safe_tray_quit
Messenger._tray_quit = _safe_tray_quit
# === END TRAY_SAVE_FIX_V4 ===


# === TRAY_SAVE_FIX_V5 ===
# Перекрываем сломанные методы из TRAY_FIX_V1, добавляем сохранение настроек и кэша
def _safe_close_v5(self, e):
    if getattr(self, "_really_close", False):
        # Реальное закрытие приложения
        try:
            save_settings()
        except Exception:
            pass
        try:
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        # Вызываем оригинальный closeEvent из QStackedWidget
        try:
            from PySide6.QtWidgets import QStackedWidget
            QStackedWidget.closeEvent(self, e)
        except Exception:
            e.accept()
    else:
        # Сворачивание в трей
        e.ignore()
        try:
            save_settings()
        except Exception:
            pass
        try:
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        self.hide()
        try:
            self.tray.showMessage("Bebsi", "Я в трее — клик по иконке вернёт окно", self.tray.icon(), 1500)
        except Exception:
            pass

def _safe_quit_v5(self):
    self._really_close = True
    try:
        save_settings()
    except Exception:
        pass
    try:
        if hasattr(self, "chat") and self.chat:
            _save_disk_cache(self.chat)
    except Exception:
        pass
    try:
        if getattr(self, "net", None):
            self.net.close()
    except Exception:
        pass
    from PySide6.QtWidgets import QApplication
    QApplication.quit()

# Перекрываем методы Messenger, чтобы перебить TRAY_FIX_V1 и PACK2
Messenger.closeEvent = _safe_close_v5
Messenger._tray_quit = _safe_quit_v5
Messenger._tf_quit = _safe_quit_v5
# === END TRAY_SAVE_FIX_V5 ===


# === TRAY_SAVE_FIX_V6 ===
# Исправление: гарантированное сохранение настроек и аккаунтов при сворачивании в трей и выходе

def _safe_close_v6(self, e):
    if getattr(self, "_really_close", False):
        # Реальное закрытие приложения
        try:
            save_settings()
        except Exception:
            pass
        try:
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        e.accept()
    else:
        # Сворачивание в трей
        e.ignore()
        try:
            save_settings()
        except Exception:
            pass
        try:
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        self.hide()
        try:
            self.tray.showMessage("Bebsi", "Я в трее — клик по иконке вернёт окно", self.tray.icon(), 1500)
        except Exception:
            pass

def _safe_quit_v6(self):
    self._really_close = True
    try:
        save_settings()
    except Exception:
        pass
    try:
        if hasattr(self, "chat") and self.chat:
            _save_disk_cache(self.chat)
    except Exception:
        pass
    try:
        if getattr(self, "net", None):
            self.net.close()
    except Exception:
        pass
    from PySide6.QtWidgets import QApplication
    QApplication.quit()

# Перекрываем методы Messenger, чтобы перебить TRAY_FIX_V1 и PACK2
Messenger.closeEvent = _safe_close_v6
Messenger._tray_quit = _safe_quit_v6
Messenger._tf_quit = _safe_quit_v6
# === END TRAY_SAVE_FIX_V6 ===


# === TRAY_SAVE_FIX_V7 ===
# Комплексное исправление: сохранение настроек + чистка трея

def _safe_close_v7(self, e):
    """Перезаписывает closeEvent из TRAY_FIX_V1 и PACK2"""
    if getattr(self, "_really_close", False):
        # Реальное закрытие
        try:
            save_settings()
        except Exception:
            pass
        try:
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        # Вызываем оригинальный closeEvent
        try:
            from PySide6.QtWidgets import QStackedWidget
            QStackedWidget.closeEvent(self, e)
        except Exception:
            e.accept()
        # Принудительно убираем иконку из трея
        try:
            self.tray.hide()
        except Exception:
            pass
    else:
        # Сворачивание в трей
        e.ignore()
        try:
            save_settings()  # <-- КЛЮЧЕВОЕ: сохраняем аккаунты
        except Exception:
            pass
        try:
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        self.hide()
        try:
            self.tray.showMessage("Bebsi", "Свёрнуто в трей", self.tray.icon(), 1500)
        except Exception:
            pass

def _safe_quit_v7(self):
    """Перезаписывает _tf_quit и _tray_quit"""
    self._really_close = True
    try:
        save_settings()  # <-- КЛЮЧЕВОЕ: сохраняем аккаунты
    except Exception:
        pass
    try:
        if hasattr(self, "chat") and self.chat:
            _save_disk_cache(self.chat)
    except Exception:
        pass
    try:
        if getattr(self, "net", None):
            self.net.close()
    except Exception:
        pass
    # Убираем иконку из трея перед выходом
    try:
        self.tray.hide()
    except Exception:
        pass
    from PySide6.QtWidgets import QApplication
    QApplication.quit()
    # Принудительное завершение через 2 секунды (чистит трей)
    import threading
    threading.Timer(2.0, lambda: os._exit(0)).start()

# Перекрываем все предыдущие патчи
Messenger.closeEvent = _safe_close_v7
Messenger._tray_quit = _safe_quit_v7
Messenger._tf_quit = _safe_quit_v7
# === END TRAY_SAVE_FIX_V7 ===


# === TRAY_SAVE_FIX_V8 ===
# Гарантированное сохранение настроек и аккаунтов при любом закрытии

def _final_close(self, e):
    """Финальная версия closeEvent - всегда сохраняет настройки"""
    if getattr(self, "_really_close", False):
        # Реальное закрытие приложения
        try:
            save_settings()
        except Exception:
            pass
        try:
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        # Вызываем оригинальный closeEvent
        try:
            from PySide6.QtWidgets import QStackedWidget
            QStackedWidget.closeEvent(self, e)
        except Exception:
            e.accept()
        # Принудительно убираем иконку из трея
        try:
            self.tray.hide()
        except Exception:
            pass
    else:
        # Сворачивание в трей
        e.ignore()
        try:
            save_settings()  # <-- КЛЮЧЕВОЕ: сохраняем аккаунты
        except Exception:
            pass
        try:
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        self.hide()
        try:
            self.tray.showMessage("Bebsi", "Свёрнуто в трей", self.tray.icon(), 1500)
        except Exception:
            pass

def _final_quit(self):
    """Финальная версия выхода - всегда сохраняет настройки"""
    self._really_close = True
    try:
        save_settings()  # <-- КЛЮЧЕВОЕ: сохраняем аккаунты
    except Exception:
        pass
    try:
        if hasattr(self, "chat") and self.chat:
            _save_disk_cache(self.chat)
    except Exception:
        pass
    try:
        if getattr(self, "net", None):
            self.net.close()
    except Exception:
        pass
    # Убираем иконку из трея перед выходом
    try:
        self.tray.hide()
    except Exception:
        pass
    from PySide6.QtWidgets import QApplication
    QApplication.quit()
    # Принудительное завершение через 2 секунды (чистит трей)
    import threading
    threading.Timer(2.0, lambda: os._exit(0)).start()

# Перекрываем ВСЕ предыдущие патчи (PACK2, TRAY_FIX_V1, CACHE_FIX_V1)
Messenger.closeEvent = _final_close
Messenger._tray_quit = _final_quit
Messenger._tf_quit = _final_quit
# === END TRAY_SAVE_FIX_V8 ===


# === FINAL_SAVE_FIX_V1 ===
# Гарантированное сохранение аккаунта через aboutToQuit и accounts.json

# 1. Хук на aboutToQuit - вызывается при ЛЮБОМ закрытии приложения
_orig_main = main
def _main_with_hook():
    _orig_main()
    
# Перехватываем создание QApplication чтобы добавить aboutToQuit
_orig_app_init = QApplication.__init__
def _app_init_hook(self, *args, **kwargs):
    _orig_app_init(self, *args, **kwargs)
    self.aboutToQuit.connect(lambda: (save_settings(), _save_disk_cache(globals().get('w', None).chat) if globals().get('w') else None))
QApplication.__init__ = _app_init_hook

# 2. Модифицируем обработку auth_ok чтобы гарантированно сохранял LAST_U и ACCOUNTS
_orig_on_packet = Messenger.on_packet
def _on_packet_save(self, pkt):
    _orig_on_packet(self, pkt)
    if pkt.get("type") == "auth_ok":
        try:
            global LAST_U, ACCOUNTS
            username = pkt.get("username", "")
            if username:
                LAST_U = username
                # Добавляем в ACCOUNTS если нет
                if not any(a.get("u") == username for a in ACCOUNTS):
                    creds = getattr(self, "creds", ("", ""))
                    if creds[1]:
                        ACCOUNTS.append({"u": username, "p": _dpapi_protect(creds[1].encode("utf-8"))})
                save_settings()
                _upd_dbg("AUTH_OK: saved LAST_U=" + username + " accounts=" + str(len(ACCOUNTS)))
        except Exception as e:
            _upd_dbg("AUTH_OK SAVE ERR: " + repr(e))
Messenger.on_packet = _on_packet_save

# 3. Модифицируем _auto_login чтобы использовал accounts.json от ACC_FIX_V1
_orig_auto_login = Messenger._auto_login
def _auto_login_v2(self):
    _upd_dbg("AUTOLOGIN_V2 ENTER last=" + repr(LAST_U) + " accounts=" + repr([a.get("u") for a in ACCOUNTS]))
    try:
        # Пробуем accounts.json от ACC_FIX_V1
        if "_acc_load" in globals() and "_dec_pw" in globals():
            d = _acc_load()
            if d:
                name = max(d.keys(), key=lambda k: d[k].get("last", 0))
                pw = _dec_pw(d[name].get("pw", ""))
                if pw:
                    _upd_dbg("AUTOLOGIN_V2: using accounts.json for " + name)
                    self.on_auth_submit("login", name, pw)
                    return
        # Фоллбэк на settings.json
        _orig_auto_login(self)
    except Exception as e:
        _upd_dbg("AUTOLOGIN_V2 ERR: " + repr(e))
        _orig_auto_login(self)
Messenger._auto_login = _auto_login_v2
# === END FINAL_SAVE_FIX_V1 ===


# === FINAL_ACCOUNT_SAVE_V1 ===
# Гарантированное сохранение аккаунта при регистрации, входе, закрытии в трей и выходе

# 1. Перехватываем on_packet чтобы сохранять аккаунт СРАЗУ после auth_ok (и при регистрации, и при входе)
_orig_on_packet_final = Messenger.on_packet
def _on_packet_final_save(self, pkt):
    _orig_on_packet_final(self, pkt)
    try:
        if pkt.get("type") == "auth_ok":
            username = pkt.get("username", "")
            if username:
                global LAST_U, ACCOUNTS
                LAST_U = username
                # Добавляем в ACCOUNTS если нет
                if not any(a.get("u") == username for a in ACCOUNTS):
                    creds = getattr(self, "creds", ("", ""))
                    if creds and len(creds) >= 2 and creds[1]:
                        pw = creds[1]
                        ACCOUNTS.append({"u": username, "p": _dpapi_protect(pw.encode("utf-8"))})
                # НЕМЕДЛЕННО сохраняем в settings.json
                save_settings()
                # Также сохраняем в accounts.json (через ACC_FIX_V1)
                try:
                    if "_acc_load" in globals() and "_acc_save" in globals() and "_enc_pw" in globals():
                        d = _acc_load()
                        pw = creds[1] if creds and len(creds) >= 2 else ""
                        if pw:
                            blob = _enc_pw(pw)
                            if blob:
                                d[username] = {"pw": blob, "last": time.time()}
                                _acc_save(d)
                except Exception:
                    pass
    except Exception:
        pass

Messenger.on_packet = _on_packet_final_save

# 2. Перебиваем TRAY_FIX_V1: добавляем save_settings() в closeEvent
def _final_close_v1(self, e):
    if getattr(self, "_really_close", False):
        try:
            save_settings()
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        try:
            from PySide6.QtWidgets import QStackedWidget
            QStackedWidget.closeEvent(self, e)
        except Exception:
            e.accept()
        try:
            self.tray.hide()
        except Exception:
            pass
    else:
        e.ignore()
        try:
            save_settings()  # <-- КЛЮЧЕВОЕ: сохраняем аккаунты перед скрытием в трей
            if hasattr(self, "chat") and self.chat:
                _save_disk_cache(self.chat)
        except Exception:
            pass
        self.hide()
        try:
            self.tray.showMessage("Bebsi", "Свёрнуто в трей", self.tray.icon(), 1500)
        except Exception:
            pass

# 3. Перебиваем TRAY_FIX_V1: добавляем save_settings() в _tf_quit
def _final_quit_v1(self):
    self._really_close = True
    try:
        save_settings()  # <-- КЛЮЧЕВОЕ: сохраняем аккаунты перед выходом
        if hasattr(self, "chat") and self.chat:
            _save_disk_cache(self.chat)
    except Exception:
        pass
    try:
        if getattr(self, "net", None):
            self.net.close()
    except Exception:
        pass
    try:
        self.tray.hide()
    except Exception:
        pass
    from PySide6.QtWidgets import QApplication
    QApplication.quit()
    import threading
    threading.Timer(2.0, lambda: os._exit(0)).start()

# Перекрываем все предыдущие патчи
Messenger.closeEvent = _final_close_v1
Messenger._tf_quit = _final_quit_v1
Messenger._tray_quit = _final_quit_v1
# === END FINAL_ACCOUNT_SAVE_V1 ===


# ============ FINAL_FIX_2024 ============
# Последний фикс — перебивает ВСЕ предыдущие патчи трея и добавляет сохранение

def _final_close_2024(self, e):
    if getattr(self, "_really_close", False):
        try: save_settings()
        except: pass
        try:
            if hasattr(self, 'chat') and self.chat:
                _save_disk_cache(self.chat)
        except: pass
        try:
            from PySide6.QtWidgets import QStackedWidget
            QStackedWidget.closeEvent(self, e)
        except:
            e.accept()
        try: self.tray.hide()
        except: pass
    else:
        e.ignore()
        try: save_settings()
        except: pass
        try:
            if hasattr(self, 'chat') and self.chat:
                _save_disk_cache(self.chat)
        except: pass
        self.hide()
        try:
            self.tray.showMessage("Bebsi", "Свёрнуто в трей", self.tray.icon(), 1500)
        except: pass

def _final_quit_2024(self):
    self._really_close = True
    try: save_settings()
    except: pass
    try:
        if hasattr(self, 'chat') and self.chat:
            _save_disk_cache(self.chat)
    except: pass
    try:
        if getattr(self, 'net', None):
            self.net.close()
    except: pass
    try: self.tray.hide()
    except: pass
    from PySide6.QtWidgets import QApplication
    QApplication.quit()
    import threading
    threading.Timer(2.0, lambda: os._exit(0)).start()

# Перебиваем ВСЕ предыдущие патчи
Messenger.closeEvent = _final_close_2024
Messenger._tf_quit = _final_quit_2024
Messenger._tray_quit = _final_quit_2024

# Исправляем автологин — делаем ОДНУ попытку вместо 12 (убираем rate limit)
if "_se_acc" in dir() or True:
    _old_se = AuthScreen.showEvent
    def _new_se(self, e):
        if getattr(self, "_acc_tried_2024", False):
            return
        self._acc_tried_2024 = True
        try:
            d = _acc_load()
            if not d:
                return
            name = max(d.keys(), key=lambda k: d[k].get("last", 0))
            pw = _dec_pw(d[name].get("pw", ""))
            if not pw:
                return
            self.u.setText(name)
            self.p.setText(pw)
            def _try_once():
                try:
                    app = self.window()
                    if getattr(app, "authed", False) or not self.isVisible():
                        return
                    net = getattr(app, "net", None)
                    ok = (net is not None and getattr(net, "sock", None) is not None)
                    if ok:
                        _PENDING_PW[name] = pw
                        self.submit.emit("login", name, pw)
                except: pass
            QTimer.singleShot(1500, _try_once)
        except: pass
    AuthScreen.showEvent = _new_se

print("✅ FINAL_FIX_2024 применён")
# ============ END FINAL_FIX_2024 ============


# === SHORTCUT_CREATOR ===
def _create_shortcut():
    """Создаёт ярлык на рабочем столе для запуска без CMD"""
    try:
        import sys, os
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        shortcut_path = os.path.join(desktop, "Bebsi.lnk")
        
        if os.path.exists(shortcut_path):
            return
        
        # Создаём .bat файл для запуска
        bat_path = os.path.join(DIR, "run_bebsi.bat")
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write('@echo off\n')
            f.write('start /min "" "' + sys.executable + '" "' + CLIENT_PATH + '"\n')
        
        # Создаём ярлык через VBScript
        vbs_path = os.path.join(DIR, "create_shortcut.vbs")
        with open(vbs_path, "w") as f:
            f.write('Set WshShell = CreateObject("WScript.Shell")\n')
            f.write('Set Shortcut = WshShell.CreateShortcut("' + shortcut_path + '")\n')
            f.write('Shortcut.TargetPath = "' + bat_path + '"\n')
            f.write('Shortcut.WorkingDirectory = "' + DIR + '"\n')
            f.write('Shortcut.IconLocation = "' + os.path.join(DIR, "bebsi.ico") + '"\n')
            f.write('Shortcut.Save\n')
        
        os.system('cscript //nologo "' + vbs_path + '"')
        print("✅ Ярлык создан на рабочем столе!")
    except Exception as e:
        print("⚠️ Не удалось создать ярлык:", e)

# Запускаем создание ярлыка при первом запуске
if not os.path.exists(os.path.join(os.path.expanduser("~"), "Desktop", "Bebsi.lnk")):
    QTimer.singleShot(2000, _create_shortcut)
# === END SHORTCUT_CREATOR ===


def _night_tick(self):
    """Проверка ночного режима каждую минуту"""
    try:
        if not NIGHT[0]:
            return
        h = datetime.now().hour
        f, t = NIGHT[1], NIGHT[2]
        active = f <= h < t if f <= t else (h >= f or h < t)
        if active and not getattr(self, "_night_state", False):
            self._night_state = True
            try:
                self.chat.apply_theme("Тёмная")
            except Exception:
                pass
        elif not active and getattr(self, "_night_state", False):
            self._night_state = False
            try:
                self.chat.apply_theme("Светлая")
            except Exception:
                pass
    except Exception:
        pass

Messenger._night_tick = _night_tick

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПока! 👋")
    except Exception:
        import traceback
        _m = traceback.format_exc()
        try:
            with open(os.path.join(DIR, "crash.log"), "a", encoding="utf-8") as f:
                f.write(_m + "\n")
        except Exception:
            pass
        try:
            import ctypes
            ctypes.windll.user32.MessageBoxW(0, _m[:2000], "Bebsi — crash", 0x10)
        except Exception:
            pass
