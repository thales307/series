def slices(series, length):
    if len(series) == 0 or series is None:
        raise ValueError('Series must be size greater than zero.')
    if length <= 0:
        raise ValueError('Length must be positive.')
    if length > len(series):
        raise ValueError('Length cannot be larger than series.')

    list_out = []

    for i in range(len(series) - length + 1):
        list_out.append(series[i:i + length])
    return list_out
