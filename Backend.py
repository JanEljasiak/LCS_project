def longest_common_subsequences(seq1, seq2):
  # Create a 2D list to store the lengths of the longest common subsequences at each index
  lengths = [[0 for j in range(len(seq2)+1)] for i in range(len(seq1)+1)]

  # Loop through the sequences and update the lengths of the longest common subsequences at each index
  for i, x in enumerate(seq1):
    for j, y in enumerate(seq2):
      if x == y:
        lengths[i+1][j+1] = lengths[i][j] + 1
      else:
        lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

  # Use the lengths list to find all longest common subsequences
  result = set()
  x, y = len(seq1), len(seq2)
  while x != 0 and y != 0:
    if lengths[x][y] == lengths[x-1][y]:
      x -= 1
    elif lengths[x][y] == lengths[x][y-1]:
      y -= 1
    else:
      result.add(seq1[x-1])
      x -= 1
      y -= 1

  # Return the set of longest common subsequences
  return result



list = longest_common_subsequences("ABCBDAB", "BDCABA")
print(list)