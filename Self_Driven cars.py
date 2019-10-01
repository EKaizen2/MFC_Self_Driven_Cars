from numpy import   *
array1 = array([2,5])
array2  = array([6,8])

magnitude1 = sqrt(array1[0]*array1[0] + array1[1]*array1[1])
magnitude2 = sqrt(array2[0]*array2[0] + array2[1]*array2[1])

print(magnitude1)
print(magnitude2)

dot_product = ((array1[0] * array2[0]) + (array1[1] * array2[1]))

vector_angle = math.acos(dot_product / (magnitude1 * magnitude2)) * 180/3.14


resultant = sqrt((magnitude1*magnitude1)*(magnitude2*magnitude2) - (2 * (magnitude1*magnitude2) * math.cos(vector_angle)))

print('Travel\n' +
      str(resultant) + '  long')

angle1 = math.atan((array1[0]) / (array1[1])) * 180/3.14
angle2 = math.atan((array2[0]) / (array2[1])) * 180/3.14

# print(angle1)
# print(angle2)


wide_angle = ((90 - angle2) + 90 + angle1)

x = math.sin(wide_angle) / resultant
resultant_angle = math.asin(x * magnitude2) * 180/3.14 + angle1

print('On a bearing of\n' +
      str(resultant_angle) + '  degrees')





















