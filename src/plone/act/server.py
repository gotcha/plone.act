import sys
import signal


def start(zope_layer_dotted_name):

    COUNT = 50

    from plone.act import Zope2ServerLibrary

    print '=' * COUNT
    print "Starting Zope 2 server"

    print "layer : {0}".format(zope_layer_dotted_name)
    print '=' * COUNT

    zsl = Zope2ServerLibrary()
    zsl.start_zope_server(zope_layer_dotted_name)
    try:
        zsl.zodb_setup()

        print '=' * COUNT
        print "Zope 2 server started"
        print "layer : {0}".format(zope_layer_dotted_name)
        print '=' * COUNT

        sys.stdout.flush()
        signal.pause()
    finally:
        zsl.zodb_teardown()
        print
        print "Stopping Zope 2 server"
        print '=' * COUNT
        zsl.stop_zope_server()
        print '=' * COUNT
        print "Zope 2 server stopped"
        print '=' * COUNT


def server():
    import sys
    try:
        start(sys.argv[1])
    except KeyboardInterrupt:
        pass
