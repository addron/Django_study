# def simple_middleware(get_response):
#     # 最先执行
#     print('init1111')
#
#     def middleware(request):
#         # 第二个
#         print('视图函数调用前执行，before')
#
#         response = get_response(request)
#         print(response)
#         # 调用后
#         print('after,调用后执行')
#         return response
#
#     return middleware
#
#
# def simple_middleware2(get_response):
#     # 最先执行
#     print('init2222')
#
#     def middleware(request):
#         # 第二个
#         print('视图函数调用前执行2，before')
#
#         response = get_response(request)
#         print(response)
#         # 调用后
#         print('after,调用后执行2')
#         return response
#
#     return middleware
