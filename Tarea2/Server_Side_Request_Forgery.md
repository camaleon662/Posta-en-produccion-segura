## INDICE

1 . Introducción

2 . Análisis de la vulnerabilidad

3 . Escenarios actuales



## 1 . Introducción

Un ataque de falsificación de solicitudes del lado del servidor (ServerSideRequestForguery), se basa en que el atacante puede modificar una URL de una solicitud legitima y lanzar consultas http que sean ejecutadas en el servidor.





## 2 . Análisis de la vulnerabilidad

Este tipo de solicitudes serian ejecutadas en el servidor y esta petición pasaría a ser una solicitud interna del mismo servidor, pudiendo acceder a recursos que solo se pueden consultar desde la red interna, por ejemplo leer la configuración de metadatos de AWS, conectarse a servicios internos como bases de datos habilitadas para http o realizar solicitudes de publicación hacia servicios internos que no están destinados a estar expuestos.





## 3 . Escenarios actuales

Un escenario actual puede ser la obtención de metadatos de AWS con este método.

Otro escenario es un ataque de denegación de servicio, pero en vez de atacar al servidor principal que esta mas protegido, atacar a un servidor interno.

Otro escenario podría ser el acceso a datos o plataformas que solo son accesibles desde la red interna.



## 4 . Practica







## 5 . Mitigación

Como medida de mitigación se debería prohibir en el codigo las peticiones que no sean http o https, asi como los accesos a redes privadas en las URL, también usar whitelist con los dominios aceptados y el uso de expresiones regulares que solo permitan lo que nuestra aplicación necesita.

Como en cualquier vulnerabilidad, también es muy importante tener los sistemas y programas actualizados, asi como tener politicas de seguridad que contemplen estos escenarios.







