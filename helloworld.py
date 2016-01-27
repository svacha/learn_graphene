# Follows the quickstart here:
# http://graphene-python.org/docs/quickstart/

import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, info):
        return 'World'

schema = graphene.Schema(query=Query)

if __name__ == '__main__':
    result = schema.execute('{ hello }')
    print result.data['hello'] # "World"
