import numpy as np

def make_uint64() -> np.uint64:
    """
    :return: an np.uint64 zero
    """
    return np.uint64(0)

def set_bit(bitboard: np.uint64, bit: int) -> np.uint64:
    """
    Sets a bit in the provided unsigned 64-bit integer bitboard representation to 1
    :param bitboard: np.uint64 number
    :param bit: the binary index to turn on
    :return: a copy of the bitboard with the `bit` set to 1
    """
    return np.uint64(bitboard | np.uint64(1) << np.uint64(bit))

def clear_bit(bitboard: np.uint64, bit: int) -> np.uint64:
    """
    Clears a bit in the provided unsigned 64-bit integer bitboard representation to 0
    :param bitboard: np.uint64 number
    :param bit: the binary index to turn off
    :return: a copy of the bitboard with the `bit` set to 0
    """
    return np.uint64(bitboard & ~(np.uint64(1) << np.uint64(bit)))