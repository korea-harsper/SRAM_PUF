#!/usr/bin/env python3
#
# Class to store memory dumps from the boards

from datetime import datetime


class Dump(object):

    def __init__(self, board_id,
                 data, mem_pos, temp, vdd,
                 temp_cal_30, temp_cal_110, vrefint_cal,
                 length=None, fd=None, timestamp=None):
        self.board_id = board_id
        self.temp = temp
        self.vdd = vdd
        self.temp_cal_30 = temp_cal_30
        self.temp_cal_110 = temp_cal_110
        self.vrefint_cal = vrefint_cal
        self.timestamp = datetime.now().strftime('%d-%m-%Y-%H:%M:%S')
        self.mem_pos = mem_pos
        self.data = data
        self.length = len(data) if length is None else length

    def __eq__(self, other):
        if self.length != other.length:
            raise ValueError("The length of the dumps is not the same")

        for i in range(0, self.length):
            if self.data[i] != other.data[i]:
                return False
        else:
            return True


def compare_dumps(dump1, dump2):
    '''
    Calculate by how much two dumps differ
    '''
    differ = 0
    if dump1.lenght != dump2.lenght:
        raise ValueError("The length of the dumps differs.")

    for i in range(0, dump1.length):
        if dump1[i] != dump2[i]:
            differ += 1
    return (differ / dump1.length) * 100
