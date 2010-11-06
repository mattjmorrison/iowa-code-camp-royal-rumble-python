from jinja2 import Environment, PackageLoader
from pesto import Response
import json

jinja_env = Environment(loader=PackageLoader('twitter'))

def to_html(template_file):
    def func_wrapper(func):
        def call_wrapper(request, *args, **kwargs):
            result = func(request, *args, **kwargs)
            if isinstance(result, dict):
                template = jinja_env.get_template(template_file)
                return Response([str(template.render(**result))])
            else:
                return result
        return call_wrapper
    return func_wrapper

def to_json(func):
    def to_json(request, *args, **kwargs):
        result = func(request, *args, **kwargs)
        if isinstance(result, Response):
            return result
        return Response(
            content=[json.dumps(result)],
            content_type='application/json'
        )
    return to_json