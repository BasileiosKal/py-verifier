import requests
import json 

token = "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJjbmYiOnsiandrIjp7ImNydiI6IkVkMjU1MTkiLCJrdHkiOiJPS1AiLCJ4IjoiNnZjRkhiem4xc0lORzQtUVlaMUlhaTNkMm1LVTF1MEtZRDNya0tobk1hbyJ9fSwiaXNzIjoiaHR0cHM6Ly96ZXJvLmNvcnAiLCJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvMjAxOC9jcmVkZW50aWFscy92MSIsImh0dHBzOi8vbW0uYXVlYi5nci9jb250ZXh0cy9hY2Nlc3NfY29udHJvbC92MSJdLCJjcmVkZW50aWFsU3ViamVjdCI6eyJDYXBhYmlsaXRpZXMiOlsiUmVhZCBJbnZlbnRvcnkiLCJXcml0ZSBJbnZlbnRvcnkiXSwidHlwZSI6WyJDYXBhYmlsaXRpZXMiXX0sImlkIjoiaHR0cHM6Ly93d3cuc29maWUtaW90LmV1L2NyZWRlbnRpYWxzL2V4YW1wbGVzLzEiLCJ0eXBlIjpbIlZlcmlmaWFibGVDcmVkZW50aWFsIl19fQ.1dVXJhv1hAY7Uhvg_DW553aSXrZYKj-15xxtzTeZXgVkUuq1JP1o6uQbzb_ABBndWPa0HVlue4G3Ulw4RIdlBg"
dpop  = "eyJhbGciOiJFZERTQSIsImp3ayI6eyJjcnYiOiJFZDI1NTE5Iiwia3R5IjoiT0tQIiwieCI6IjZ2Y0ZIYnpuMXNJTkc0LVFZWjFJYWkzZDJtS1UxdTBLWUQzcmtLaG5NYW8ifSwidHlwIjoiZHBvcCtqd3QifQ.eyJodG0iOiJHRVQiLCJodHUiOiJodHRwczovL3JlbW90ZS5jbG91ZC96ZXJvY29ycCIsImlhdCI6MTU2MjI2MjYxNiwianRpIjoiLUJ3QzNFU2M2YWNjMmxUYyJ9.GGq1Kg9BJN6O6s49_NGIhbM15f6soF4flHoyVIA4HpghVxtA9O-J9-VC6mICQPHB1hWnTDQd3ZGnJ7BAWfvECA"
headers = {'Authorization':'DPoP ' + token, 'Accept': 'application/json', 'dpop':dpop}
response  = requests.get("http://localhost:9000/secure/jwt-vc-dpop", headers = headers)
print(response.text)