## -*- coding: UTF-8 -*-
## index.py
##
## Copyright (c) 2018 analyzeDFIR
## 
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
## 
## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.
## 
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

from construct import *

try:
    from shared_structures.windows.misc import NTFSFileReference
except ImportError:
    from .shared_structures.windows.misc import NTFSFileReference

'''
MFTIndexValue
'''
MFTIndexEntry = Struct(
    'FileReference'     / NTFSFileReference,
    'IndexValueSize'    / Int16ul,
    'IndexKeyDataSize'  / Int16ul,
    'Flags'             / FlagsEnum(Int32ul,
        HAS_SUB_NODE    = 0x00000001,
        IS_LAST         = 0x00000002\
    )
)

'''
MFTIndexNodeHeader
'''
MFTIndexNodeHeader = Struct(
    'IndexValuesOffset'         / Int32ul,
    'IndexNodeSize'             / Int32ul,
    'AllocatedIndexNodeSize'    / Int32ul,
    'Flags'                     / FlagsEnum(Int32ul,
        HasIndexAllocation = 0x00000001\
    )
)

'''
MFTIndexEntryHeader
'''
MFTIndexEntryHeader = Struct(
    'Signature'             / Const(b'INDX'),
    'FixupValuesOffset'     / Int16ul,
    'FixupValuesCount'      / Int16ul,
    'LogFileSequenceNumber' / Int64ul,
    'VirtualClusterNumber'  / Int64ul
)

'''
MFTIndexRootCollationType
'''
MFTIndexRootCollationType = Enum(Int32ul,
    COLLATION_BINARY                = 0x00000000,
    COLLATION_FILENAME              = 0x00000001,
    COLLATION_UNICODE_STRING        = 0x00000002,
    COLLATION_NTOFS_ULONG           = 0x00000010,
    COLLATION_NTOFS_SID             = 0x00000011,
    COLLATION_NTOFS_SECURITY_HASH   = 0x00000012,
    COLLATION_NTOFS_ULONGS          = 0x00000013
)

'''
MFTIndexRootHeader
'''
MFTIndexRootHeader = Struct(
    'AttributeType'                 / Int32ul,
    'CollationType'                 / MFTIndexRootCollationType,
    'IndexAllocationEntrySize'      / Int32ul,
    'IndexRecordClusterBlockCount'  / Int32ul
)
