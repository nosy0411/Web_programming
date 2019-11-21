import dio

response = await dio.get<List<dynamic>>("https://vod2.icampus.ac.kr/testservice.svc/GetHaksa_login", queryParameters : {"uid":uid, "pwd":pwd}, options : Options(responseType: ResponseType.json))

print(response.data)
print(response.headers)
print(response.request)
print(response.statusCode)