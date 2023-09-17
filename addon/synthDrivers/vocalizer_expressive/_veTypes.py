#vocalizer/_veTypes.py
#A part of the vocalizer driver for NVDA (Non Visual Desktop Access)
#Copyright (C) 2012 Rui Batista <ruiandrebatista@gmail.com>
#Copyright (C) 2012 - 2023 Tiflotecnia, lda. <www.tiflotecnia.net>
#This file is covered by the GNU General Public License.
#See the file GPL.txt for more details.

from ctypes import *


#Constant definitions
VE_CURRENT_VERSION = 0x0520
VE_MAX_STRING_LENGTH = 128
VPLATFORM_CURRENT_VERSION = 0x0200

# Error codes
NUAN_OK = 0
NUAN_E_TTS_USERSTOP = 0x80000807
NUAN_E_WRONG_STATE = 0x80000011
NUAN_E_NOTFOUND = 0x80000014

# NVDA license specific codes
VAUTONVDA_ERROR_INVALID = 0XF1
VAUTONVDA_ERROR_CRYPTO = 0XF2
VAUTONVDA_ERROR_IO = 0XF3
VAUTONVDA_ERROR_NOLICENSE = 0XF4
VAUTONVDA_ERROR_EXPIRED = 0XF5
VAUTONVDA_ERROR_INVALID_TOKEN = 0XF6
VAUTONVDA_ERROR_DEMO_EXPIRED = 0xFF


# Text formats
VE_NORM_TEXT = 0
VE_HTML_TEXT = 1
VE_XML_TEXT = 2
VE_SSML_TEXT = 3

# Parameter ids
VE_PARAM_FREQUENCY            = 1
VE_PARAM_VOLUME               = 2
VE_PARAM_SPEECHRATE           = 3
VE_PARAM_PITCH                = 4
VE_PARAM_WAITFACTOR           = 5
VE_PARAM_READMODE             = 6
VE_PARAM_LANGUAGE             = 7
VE_PARAM_VOICE                = 8
VE_PARAM_PPMODE               = 9
VE_PARAM_MSGMODE              = 10
VE_PARAM_TYPE_OF_CHAR         = 11
VE_PARAM_MARKER_MODE          = 12
VE_PARAM_INITMODE             = 13
VE_PARAM_TEXTMODE             = 14
VE_PARAM_LANGUAGE_NR          = 15
VE_PARAM_DPLEX_MAXSIZE        = 16
VE_PARAM_DPLEX_MAXMSGS        = 17
VE_PARAM_MAX_INPUT_LENGTH     = 18
VE_PARAM_VOICE_MODEL          = 19
VE_PARAM_LIDSCOPE             = 20
VE_PARAM_LIDVOICESWITCH       = 21
VE_PARAM_EXTRAESCLANG         = 22
VE_PARAM_EXTRAESCTN           = 23
VE_PARAM_LIDMODE = 24
VE_PARAM_LIDLANGUAGES = 25


# Init Modes
VE_INITMODE_LOAD_ONCE_OPEN_ALL = 0xC
VE_INITMODE_LOAD_OPEN_ALL_EACH_TIME = 0x3

# Text modes
VE_TEXTMODE_STANDARD = 1
VE_TEXTMODE_SMS = 2

# Reading modes
VE_READMODE_SENT = 1
VE_READMODE_CHAR = 2
VE_READMODE_WORD = 3
VE_READMODE_LINE = 4

# Marker modes
VE_MRK_OFF = 0
VE_MRK_ON = 1


# LID voice switch
VE_LIDVOICESWITCH_OFF = 0
VE_LIDVOICESWITCH_ON = 1

# LId mode
VE_LIDMODE_MEMORY_BIASED = 0
VE_LIDMODE_FORCED_CHOICE = 1


# Message types
VE_MSG_BEGINPROCESS   = 0x00000001
VE_MSG_ENDPROCESS     = 0x00000002
VE_MSG_INTEXTREQ      = 0x00000004
VE_MSG_OUTBUFREQ      = 0x00000008
VE_MSG_OUTBUFDONE     = 0x00000010
VE_MSG_STOP           = 0x00000020
VE_MSG_PAUSE          = 0x00000040
VE_MSG_RESUME         = 0x00000080
VE_MSG_BACKWARD       = 0x00000100
VE_MSG_FORWARD        = 0x00000200
VE_MSG_TEXTUNIT       = 0x00000400
VE_MSG_WORD           = 0x00000800
VE_MSG_PHONEME        = 0x00001000
VE_MSG_BOOKMARK       = 0x00002000
VE_MSG_ERROR          = 0x00004000
VE_MSG_PROCESS        = 0x00008000
VE_MSG_TAIBEGIN       = 0x00010000
VE_MSG_TAIEND         = 0x00020000
VE_MSG_TAIBUFREQ      = 0x00040000
VE_MSG_TAIBUFDONE     = 0x00080000

# Mark types
VE_MRK_BOOKMARK= 0x0008

# Character encodings
VE_TYPE_OF_CHAR_UTF16   = 1
VE_TYPE_OF_CHAR_UTF8    = 2

# PCM State
VE_PCMSTAT_TXTUNIT_NEW = 1
VE_PCMSTAT_TXTUNIT_MID = 2
VE_PCMSTAT_DONE = 0xFFFF

# Vocalizer gives  us sample rates in khz on an enumeration.
# We need those in hz, so this is the conversion table.
sampleRateConversions = {8 : 8000,
	11 : 11025,
	16 : 16000,
	22 : 22050}


# type Definitions
class VE_HSAFE(Structure):
	_fields_ = (('pHandleData', c_void_p),
	('u32Check', c_uint))
	def __eq__(self, other):
		return addressof(self) == addressof(other) or self.pHandleData == other.pHandleData

	def __hash__(self):
		return addressof(self) ^ self.pHandleData

class VE_INSTALL(Structure):
	_fields_ = (('fmtVersion', c_ushort),
	('pBinBrokerInfo', c_char_p),
	('pIHeap', c_void_p),
	('hHeap', c_void_p),
	('pICritSec', c_void_p),
	('hCSClass', c_void_p),
	('pIDataStream', c_void_p),
	('pIDataMapping', c_void_p),
	('hDataClass', c_void_p),
	('pILog', c_void_p),
	('hLog', c_void_p))

class VPLATFORM_MEMBLOCK(Structure):
	_fields_ = [('start', c_void_p),
	('cByte', c_uint),
	('cFlags', c_uint)]

class VPLATFORM_RESOURCES(Structure):
	_fields_ = (('fmtVersion', c_ushort),
	('u16NbrOfDataInstall', c_ushort),
	('customData', POINTER(c_wchar_p)),
	('apDataInstall', POINTER(c_wchar_p)),
	('stHeap', VPLATFORM_MEMBLOCK),
	('pDatPtr_Table', c_void_p),
	('licenseToken', c_char_p),
	('licenseTokenLen', c_int),
	('licensor', c_int),
	('sessionKey', c_char_p),
	('sessionKeyLen', c_int),
	('szBinaryBroker', c_wchar_p),
	('szFileListFile', c_wchar_p),
	('rfu1', c_uint),
	('rfu2', c_uint))

class VE_INTEXT(Structure):
	_fields_ = (('eTextFormat;  ', c_int),
	('ulTextLength', c_uint),
	('szInText', c_void_p))

class VE_LPARAM(Union):
	_fields_ = (('lValue', c_uint),
	('lError', c_uint))

class VE_PARAM_VALUE(Union):
	_fields_ = (('usValue', c_ushort),
	('szStringValue', (c_char * VE_MAX_STRING_LENGTH)))

class VE_PARAM(Structure):
	_fields_ = (('ID', c_uint),
	('uValue', VE_PARAM_VALUE))

class VE_CALLBACKMSG(Structure):
	_fields_ = (('eMessage', c_uint),
	('uParam', VE_LPARAM),
	('pParam', c_void_p))

VE_CBOUTNOTIFY = CFUNCTYPE(c_uint, VE_HSAFE, c_void_p, POINTER(VE_CALLBACKMSG), c_void_p)

class VE_OUTDEVINFO(Structure):
	_fields_ = (('hOutDevInstance', c_void_p),
	('pfOutNotify', VE_CBOUTNOTIFY))

class VE_LANGUAGE(Structure):
	_fields_ = (('szLanguage', (c_char * VE_MAX_STRING_LENGTH)),
	('szLanguageTLW', (c_char * 4)),
	('szVersion', (c_char * VE_MAX_STRING_LENGTH)),
	('u16LangId', c_ushort))

class VE_VOICEINFO(Structure):
	_fields_ = (('szVersion', (c_char * VE_MAX_STRING_LENGTH)),
	('szLanguage', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceName', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceAge', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceType', (c_char * VE_MAX_STRING_LENGTH)),
	('u16LangId', c_ushort))

	def __eq__(self, other):
		return isinstance(other, type(self)) and addressof(self) == addressof(other)

class VE_SPEECHDBINFO(Structure):
	_fields_ = (('szVersion', (c_char * VE_MAX_STRING_LENGTH)),
	('szLanguage', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceName', (c_char * VE_MAX_STRING_LENGTH)),
	('szVoiceModel', (c_char * VE_MAX_STRING_LENGTH)),
	('u16Freq', c_ushort),
	('u16LangId', c_ushort))

class VE_MARKINFO(Structure):
	_fields_ = [('ulMrkInfo', c_uint),
	('eMrkType', c_uint),
	('ulSrcPos', c_uint),
	('ulSrcTextLen', c_uint),
	('ulDestPos', c_uint),
	('ulDestLen', c_uint),
	('usPhoneme', c_ushort),
	('ulMrkId', c_uint),
	('ulParam', c_uint),
	('szPromptID', c_char_p)]

class VE_OUTDATA(Structure):
	_fields_ = (('eAudioFormat', c_uint),
	('ulPcmBufLen', c_uint),
	('pOutPcmBuf', c_void_p),
	('ulMrkListLen', c_uint),
	('pMrkList', POINTER(VE_MARKINFO)))


	# FIXME:: remove this definitions if sure that don't need them anymore
# Nuance logging facilities sufix for our debugging purposes.
pfErrorFuncType = CFUNCTYPE(None, VE_HSAFE, c_uint, c_uint, POINTER(c_char_p), POINTER(c_char_p))
pfDiagnosticFuncType = CFUNCTYPE(None, VE_HSAFE, c_uint, c_char_p)
class VE_LOG_INTERFACE_S(Structure):
	_fields_ = [('pfError', pfErrorFuncType),
	('pfDiagnostic', pfDiagnosticFuncType)]

# Licenseing stuff (Tiflotecnia):
VALIDATION_LICENSED = 0
VALIDATION_DEMO = 1
VALIDATION_INVALID = 3


class LicenseRenewInfo(Structure):
	_fields_ = (('expiresTime', c_longlong),
	('renewTime', c_longlong),
	('token' , c_wchar_p))

class LicenseInfo(Structure):
	_fields_ = (('userName', c_wchar_p),
	('userId', c_wchar_p),
	('email', c_wchar_p),
	('distributor', c_wchar_p),
	('number', c_long),
	('renewInfo', POINTER(LicenseRenewInfo)))

class ValidationInfoUnion(Union):
	_fields_ = (('licenseInfo', LicenseInfo),
	('demoExpiration', c_longlong))

class ValidationInfo(Structure):
	_fields_ = (('type', c_long),
		('info', ValidationInfoUnion))

# Error handling
class VeError(RuntimeError):
	def __init__(self, code, msg):
		self.code = code
		super(RuntimeError, self).__init__(msg)

def veCheckForError(result, func, args):
	""" Checks for errors in a function from the vocalizer dlls and platform.
	
	If the error code is not positive it throws a runtime error.
	The error codes have no description, see the vocalizer SDK
	For reference."""
	if result  not in (NUAN_OK, NUAN_E_TTS_USERSTOP):
		raise VeError(result, "Vocalizer Error: %s: %x" %(func.__name__, result))

# Load Libraries
def loadVeDll(path):
	veDll = cdll.LoadLibrary(path)
	# Basic runtime type checks...
	veDll.ve_ttsInitialize.errcheck = veCheckForError
	veDll.ve_ttsInitialize.restype = c_uint
	veDll.ve_ttsOpen.errcheck = veCheckForError
	veDll.ve_ttsOpen.restype = c_uint
	veDll.ve_ttsOpen.argtypes = (VE_HSAFE, c_void_p, c_void_p, POINTER(VE_HSAFE), c_void_p)
	veDll.ve_ttsProcessText2Speech.errcheck = veCheckForError
	veDll.ve_ttsProcessText2Speech.restype = c_uint
	veDll.ve_ttsStop.errcheck = veCheckForError
	veDll.ve_ttsStop.restype = c_uint
	veDll.ve_ttsPause.errcheck = veCheckForError
	veDll.ve_ttsPause.restype = c_uint
	veDll.ve_ttsResume.errcheck = veCheckForError
	veDll.ve_ttsResume.restype = c_uint
	veDll.ve_ttsSetParamList.errcheck = veCheckForError
	veDll.ve_ttsSetParamList.restype = c_uint
	veDll.ve_ttsGetParamList.errcheck = veCheckForError
	veDll.ve_ttsGetParamList.restype = c_uint
	veDll.ve_ttsGetLanguageList.errcheck = veCheckForError
	veDll.ve_ttsGetLanguageList.restype = c_uint
	veDll.ve_ttsGetVoiceList.restype = c_uint
	veDll.ve_ttsGetVoiceList.errcheck = veCheckForError
	veDll.ve_ttsGetSpeechDBList.restype = c_uint
	veDll.ve_ttsGetSpeechDBList.errcheck = veCheckForError
	veDll.ve_ttsClose.restype = c_uint
	veDll.ve_ttsClose.errcheck = veCheckForError
	veDll.ve_ttsUnInitialize.restype = c_uint
	veDll.ve_ttsUnInitialize.errcheck = veCheckForError
	veDll.ve_ttsSetOutDevice.errcheck = veCheckForError
	veDll.ve_ttsSetOutDevice.restype = c_uint
	veDll.ve_ttsResourceLoad.errcheck = veCheckForError
	veDll.ve_ttsResourceLoad.restype = c_uint
	return veDll

def loadPlatformDll(path):
	platformDll = cdll.LoadLibrary(path)
	platformDll.vplatform_GetInterfaces.errcheck = veCheckForError
	platformDll.vplatform_GetInterfaces.restype = c_uint
	platformDll.vplatform_GetInterfaces.argtypes = (POINTER(VE_INSTALL), POINTER(VPLATFORM_RESOURCES))
	platformDll.vplatform_ReleaseInterfaces.errcheck = veCheckForError
	platformDll.vplatform_ReleaseInterfaces.restype = c_uint
	platformDll.VAUTONVDA_getLicenseInfo.errcheck = veCheckForError
	platformDll.VAUTONVDA_getLicenseInfo.restype = c_uint
	return platformDll
