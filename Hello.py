# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import random
from streamlit.logger import get_logger


LOGGER = get_logger(__name__)


def run():
    while True:
    st.set_page_config(
        page_title="Temperature e pressioni",
        page_icon="👋",
    )

    st.write("# Esempio dashboard con visuliazzazione T e P")
    T = random.randint(10, 30)
    P = random.radint(1,5)
    temperature=st.container()
    pressure=st.container()
    temperature.write(T)
    pressure.write(P)
    

    



if __name__ == "__main__":
    run()
