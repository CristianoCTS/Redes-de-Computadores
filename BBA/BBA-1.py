# -*- coding: utf-8 -*-
"""
@authors: Cristiano Tolentino Santos, Luísa Gabriela Ferro da Frota e Vinicius Alves de Araújo Lima

@description: PyDash Project

An implementation example of a Buffer based R2A Algorithm.

"""

from player.parser import *
from r2a.ir2a import IR2A


class R2AFixed(IR2A):

    def __init__(self, id):
        IR2A.__init__(self, id)
        self.parsed_mpd = ''
        self.qi = []
        self.buffer = []

    def handle_xml_request(self, msg):
        self.send_down(msg)

    def handle_xml_response(self, msg):
        self.parsed_mpd = parse_mpd(msg.get_payload())
        self.qi = self.parsed_mpd.get_qi()
        self.buffer = self.whiteboard.get_playback_buffer_size() 

        self.send_up(msg)

    def handle_segment_size_request(self, msg):
        if len(self.buffer)>0:
            # ahead is the amount of buffer the client will consume during the next X seconds
            ahead = 30
            reservoir = (ahead - self.buffer[-1][1]) if (ahead - self.buffer[-1][1]) > 10 else 10
            # buffer[0] é o tamanho do reservatório inferior e buffer[1] é o tamanho do reservatório superior
            buffer = [reservoir,50]
            print(f"Buffer size: {self.buffer[-1][1]}")
            print(f"Reservoir size: {reservoir}")
            if self.buffer[-1][1] <= buffer[0]:
                msg.add_quality_id(self.qi[0])
            elif buffer[1] >= self.buffer[-1][1] > buffer[0]:
                msg.add_quality_id(self.qi[(int((self.buffer[-1][1]-buffer[0])*(19/(buffer[1]-buffer[0]))))])
            else:
                msg.add_quality_id(self.qi[19])
        else:
            msg.add_quality_id(self.qi[0])

        self.send_down(msg)

    def handle_segment_size_response(self, msg):
        self.buffer = self.whiteboard.get_playback_buffer_size()
        self.send_up(msg)

    def initialize(self):
        pass

    def finalization(self):
        pass
