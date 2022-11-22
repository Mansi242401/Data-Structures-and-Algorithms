
class solution:
  def binary_search(self,input_array:list[int],value:int) -> int:
    n = len(input_array)
    l,r = 0,n-1
    while l <= r:
      mid = (l+r) // 2
      if value == input_array[mid]:
        return mid
      elif value > input_array[mid]:
        l = mid+1
      else:
        r = mid-1
     return -1
        
