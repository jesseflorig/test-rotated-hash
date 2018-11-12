import hashlib

input = "novetta"
hash = "135affe834f215d21a4602ec382901873e877b23" # novetta, offset 0
# hash = "1873e877b23135affe834f215d21a4602ec38290" # novetta, offset 11
# hash = "1657f58dbdaf772d1d8d4dc128658e99e4e14f61" # ???


def h_rule():
  """ print horizontal rule """
  print('=') * 80


def test_hash(input, hash):
  """ check if SHA1 hash of input = hash """
  new_hash = hashlib.sha1()
  new_hash.update(input)
  return new_hash.hexdigest() == hash


def rotate(input, offset=0):
  """ return the rotated string by offset """
  return '%s%s' % (input[offset:], input[:offset])


def test_rotated_hash(input, hash, debug=False):
  """ Check the input agaisnt every rotation of the hash """
  print("Checking %s against a roation of %s" % (input, hash))
  hash_len = len(hash)
  for idx in range(0,hash_len-1):
    rot_hash = rotate(hash, idx)
    result = test_hash(input, rot_hash)
    if(debug):
      print('checking %s against %s...' % (input, rot_hash))

    if(result):
      h_rule()
      print('SUCCESS: %s hashes to %s (offset %s)' % (input, rot_hash, idx))
      h_rule()
    else:
      if(debug):
        print('FAIL: %s hashed to %s' % (input, result))

  print("Finished testing %s iterations." % hash_len)

test_rotated_hash(input,hash,)
