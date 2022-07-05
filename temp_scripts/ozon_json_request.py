post_url = 'https://www.ozon.ru/api/composer-api.bx/widget/json/v2'

rq = {
    "asyncData": "eyJ1cmwiOiIvcHJvZHVjdC9 mb25hci1ha2t1bXVseWF0b3JueXktc3ZldG9kaW9kbnl5LXRhNC10cm9maS1mb25hci1rZW1waW5nb3Z5eS1tb3NoY2hueXktcnVjaG5veS0yMTcwOTQxMjIvP2FkdmVydD14bWFqNnIycWNYTDR3bl8yYmZKZU1GRkxQajNBdGdESlZaaFJPTEJnaTI3V3FoSG1mcHlnSDBEdDFVQmJtNms1OXhnNFN2NEhvV2E5Z2xRSGFsUFFDU3E4cWxPRDlsVDhLaGRLck13MTZ3amdoNXhMJnNoPWJzM3QtdEVIWkEiLCJjaSI6eyJuYW1lIjoid2ViUmV2aWV3UHJvZHVjdFNjb3JlIiwidmVydGljYWwiOiJycFByb2R1Y3QiLCJwYXJhbXMiOlt7Im5hbWUiOiJkaXNwbGF5VHlwZSIsInRleHQiOiJzaW1wbGUifSx7Im5hbWUiOiJhbmNob3JVcmwiLCJ0ZXh0IjoiP3RhYj1yZXZpZXdzI2NvbW1lbnRzLS1vZmZzZXQtOTAifV0sImlkIjo3MjY0MTcsInZlcnNpb24iOjF9fQ=="}

o2 = {
    "asyncData": "eyJ1cmwiOiIvcHJvZHVjdC9 rZWR5LWFkaWRhcy1hZHZhbnRhZ2UtMjczNjI5NjA0Lz9sYXlvdXRfY29udGFpbmVyPXBkcFJldmlld3MmbGF5b3V0X3BhZ2VfaW5kZXg9MiZzaD1iczN0LXVzcW1BIiwiY2kiOnsibmFtZSI6Imxpc3RSZXZpZXdzRGVza3RvcCIsInZlcnRpY2FsIjoicnBQcm9kdWN0IiwicGFyYW1zIjpbeyJuYW1lIjoicGFnaW5hdGlvblR5cGUiLCJ0ZXh0IjoibG9hZE1vcmVCdXR0b24ifSx7Im5hbWUiOiJzb3J0aW5nVHlwZSIsInRleHQiOiJ1c2VmdWxuZXNzX2Rlc2MifSx7Im5hbWUiOiJwYXJhbVBhZ2VTaXplIiwiaW50IjoxMH0seyJuYW1lIjoicGFyYW1WYXJpYW50TW9kZUVuYWJsZWQifSx7Im5hbWUiOiJ2aWRlb0FsbG93ZWQiLCJib29sIjp0cnVlfV0sImlkIjo0Mjg1NjUsInZlcnNpb24iOjF9fQ==",
    "extraBody": true}

curl
"https://www.ozon.ru/api/composer-api.bx/widget/json/v2" - X
POST - H
"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0" - H
"Accept: application/json" - H
"Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3" - H
"Accept-Encoding: gzip, deflate, br" - H
"Content-Type: application/json" - H
"x-o3-app-name: dweb_client" - H
"x-o3-app-version: release_5-6'-'2022_9ceba2ce" - H
"Origin: https://www.ozon.ru" - H
"Sec-Fetch-Dest: empty" - H
"Sec-Fetch-Mode: cors" - H
"Sec-Fetch-Site: same-origin" - H
"Referer: https://www.ozon.ru/product/kedy-adidas-advantage-273629604/?sh=bs3t-usqmA" - H
"Connection: keep-alive" - H
"Cookie: __Secure-access-token=3.0.p4sh6TsPQSO72uIHzTyBsQ.79.l8cMBQAAAABhXURRJIXrmaN3ZWKgAICQoA..20220705162406.R5a7OVqCB2c-WTCe_g8w2XDVKdd7xTYwqFs4vWh4P-4; __Secure-refresh-token=3.0.p4sh6TsPQSO72uIHzTyBsQ.79.l8cMBQAAAABhXURRJIXrmaN3ZWKgAICQoA..20220705162406.fNUvQpzaM2hS5Dgi4Iq8561OaC9XA5cprYLKyVM8kQY; __Secure-ab-group=79; __Secure-user-id=0; __Secure-ext_xcid=f03ccecdaa032a8e6497886690ea6a8f; visid_incap_1101384=Eojf3UOURnyIEDyUKgTwt1BEXWEAAAAAQUIPAAAAAAB0QO0FDEGR2/m6XGRavvej; _ga_JNVTMNXQ6F=GS1.1.1657036375.11.1.1657037095.56; _ga=GA1.1.1572177722.1633502294; cnt_of_orders=0; isBuyer=0; tmr_reqNum=172; tmr_lvid=551407eba7241ba5510f038fa321e7ff; tmr_lvidTS=1633502294650; __exponea_etc__=1055a6ac-2285-4467-a365-08eb6ae0d0b3; cto_bundle=zwCNXF9MNVRLUlU0S0s5UHJYVGNUaXRsRFJDWjZaZ3hQcVlaM0tmaUFobndYVEJBR2lWJTJGTnhLeTdmcUplODclMkY1YkxDR1U2WlpuUzRPUkZNSHA2MyUyQllXM2FqOFdzSFZxM1JWdlJseFVkNWxkZ0g4U2hYWkNERk91ZnI3ekdzNWJKMnNSeSUyRlQ2cFdzNm1lRTRkUlF4S2h5ZyUyQmdkTFlFRHlNTkJrUWVFRWJEN3hqRHZZJTNE; _gcl_au=1.1.1279983674.1654154696; tmr_detect=0" % "7C1657037097743; AREA_ID=5911; xcid=a34a9799fa7d2814b732b609dfc2c770; __cf_bm=AqGA_W55riiwydCkr48zxqmoQt8wOeSymmASIhZZUJg-1657036373-0-AV95nDYZIWkcoqrmnguwPls+Tt0uZQ/799juy7QluKm+saxueVQxFDAigKnylZesL8ldrYulM7f0VagXq+niGX/6FZtYg40knVC2Kn0b/2ect2mzN48aQrQBDM8JkbMaMfZzWaE5s29D2d4t+i5stb3++H61dsmKmi0NstVobAJJ; __exponea_time2__=-1.1165704727172852" - H
"TE: trailers" - -data - raw
"{""asyncData"":""eyJ1cmwiOiIvcHJvZHVjdC9rZWR5LWFkaWRhcy1hZHZhbnRhZ2UtMjczNjI5NjA0Lz9sYXlvdXRfY29udGFpbmVyPXBkcFJldmlld3MmbGF5b3V0X3BhZ2VfaW5kZXg9MiZzaD1iczN0LXVzcW1BIiwiY2kiOnsibmFtZSI6Imxpc3RSZXZpZXdzRGVza3RvcCIsInZlcnRpY2FsIjoicnBQcm9kdWN0IiwicGFyYW1zIjpbeyJuYW1lIjoicGFnaW5hdGlvblR5cGUiLCJ0ZXh0IjoibG9hZE1vcmVCdXR0b24ifSx7Im5hbWUiOiJzb3J0aW5nVHlwZSIsInRleHQiOiJ1c2VmdWxuZXNzX2Rlc2MifSx7Im5hbWUiOiJwYXJhbVBhZ2VTaXplIiwiaW50IjoxMH0seyJuYW1lIjoicGFyYW1WYXJpYW50TW9kZUVuYWJsZWQifSx7Im5hbWUiOiJ2aWRlb0FsbG93ZWQiLCJib29sIjp0cnVlfV0sImlkIjo0Mjg1NjUsInZlcnNpb24iOjF9fQ=="",""extraBody"":true}"
