def parcourLargeur(arbre):
  f = []
  liste = []
  f.insert(0, arbre)
  while f:
    tmp = f.pop()
    liste.append(tmp[0])
    if tmp[1] != tmp[0]:
      f.insert(0, tmp[1])
    if tmp[2] != tmp[0]:
      f.insert(0, tmp[2])
  return liste