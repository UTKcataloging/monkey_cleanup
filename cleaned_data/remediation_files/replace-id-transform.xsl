<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    
    <xsl:output method="xml" indent="yes" encoding="UTF-8"/>
    
    <xsl:template match="*|@*">
        <xsl:copy>
            <xsl:apply-templates select="*|@*|text()"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="text()">
        <!-- <xsl:copy>
            <xsl:value-of select="replace(replace(., '\\n', ''), '\\', '')"/>
        </xsl:copy> -->
        <xsl:sequence select="replace(replace(., '\\n', ''), '\\', '')"/>
        <!--<xsl:copy-of select="replace(replace(., '\\n', ''), '\\', '')"/>-->
    </xsl:template>
</xsl:stylesheet>