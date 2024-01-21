#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sys
import traceback
from llm_client import *

# settting of import messaging
sys.path.append("messaging")
from messaging import *


class LLMInstanceService:
    def __init__(self):
        default_prompt = ""
        self.llm_client = get_client_class()(default_prompt)

    def main_loop(self):
        while True:
            try:
                self.unit_work()
            except Exception as e:
                print(f"An error occurred while unit work: {e}")
                traceback.print_exc()

            time.sleep(10)

    def _make_response_and_publish(self, original_record, result):
        original_record.result = result
        rec = original_record
        LLMInstanceResMessaging().connect_and_basic_publish_record(rec)

    def unit_work(self):
        print("Getting new req from queue")
        rec = LLMInstanceReqMessaging().connect_and_basic_get_record()
        if rec is None:
            return

        result = self.llm_client.ask(rec.instruction, rec.input_)

        self._make_response_and_publish(rec, result)


# print(WhisperAndPyannote().analyze("../rec1.wav"))
LLMInstanceService().main_loop()
