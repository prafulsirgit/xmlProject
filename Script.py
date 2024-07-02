from lxml import etree

# Load XML schema
with open('document.xsd', 'rb') as f:
    schema_root = etree.XML(f.read())
schema = etree.XMLSchema(schema_root)

# Parse XML file
with open('documents.xml', 'rb') as f:
    xml_root = etree.XML(f.read())

# Validate XML against the schema
if schema.validate(xml_root):
    print("XML document is valid.")
else:
    print("XML document is invalid.")
    print(schema.error_log)

# XSLT Transformation
xslt_str = '''<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Document List</h2>
                <table border="1">
                    <tr>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Date Created</th>
                    </tr>
                    <xsl:for-each select="Documents/Document">
                        <tr>
                            <td><xsl:value-of select="Title"/></td>
                            <td><xsl:value-of select="Author"/></td>
                            <td><xsl:value-of select="DateCreated"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
'''
xslt_root = etree.XML(xslt_str)
transform = etree.XSLT(xslt_root)

# Transform the XML document
result_tree = transform(xml_root)

# Output the transformed HTML
with open('documents.html', 'wb') as f:
    f.write(etree.tostring(result_tree, pretty_print=True, method='html'))
