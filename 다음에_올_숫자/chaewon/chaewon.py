def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
      return int((common[0]) + (len(common)) * (common[2] - common[1]))
    elif common[1]/common[0] == common[2]/common[1]:
      return int((common[0]) * ((common[2]/common[1]) ** (len(common))))
