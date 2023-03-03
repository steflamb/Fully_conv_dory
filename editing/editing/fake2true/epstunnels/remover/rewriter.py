# 
# Author(s):
# Matteo Spallanzani <spmatteo@iis.ee.ethz.ch>
# 
# Copyright (c) 2020-2022 ETH Zurich and University of Bologna.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 

from .finder import EpsTunnelRemoverFinder
from .applier import EpsTunnelRemoverApplier
from quantlib.editing.editing.editors import Rewriter
from quantlib.editing.graphs.fx import quantlib_symbolic_trace


class EpsTunnelRemover(Rewriter):

    def __init__(self):
        super(EpsTunnelRemover, self).__init__('EpsTunnelRemover',
                                               quantlib_symbolic_trace,
                                               EpsTunnelRemoverFinder(),
                                               EpsTunnelRemoverApplier())
