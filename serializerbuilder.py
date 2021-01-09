import pickle
import random
import marshal
import dill
import types




def main():

  codeb = "\xe3\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00C\x00\x00\x00s\x14\x00\x00\x00t\x00\xa0\x01d\x01d\x02\xa1\x02}\x02|\x02d\x03\x1b\x00S\x00)\x04N\xe9\xdc\x00\x00\x00\xe9z\x03\x00\x00\xe9\n\x00\x00\x00)\x02\xda\x06random\xda\x07randint)\x03\xda\x0cfileLocation\xda\x06userID\xda\x04rand\xa9\x00r\t\x00\x00\x00\xfaT/Users/melandias/PycharmProjects/Dheergayu-Backend-NightlyBuild/serializerbuilder.py\xda\x0estaticFunction\x07\x00\x00\x00s\x04\x00\x00\x00\x00\x01\x0c\x01"
  staticFunction = "function_code"
  byteload = marshal.dumps(staticFunction.__code__)
  pickle.dump(byteload, open('serialize_model.pickle', 'wb'))
  print(byteload)

  code = marshal.loads(byteload)
  func = types.FunctionType(code, globals(), "some_func_name")
  print(str(func('s','s')))








if __name__ == "__main__":
  main()