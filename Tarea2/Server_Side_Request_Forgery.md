## INDICE

1 . [Introducción](#introduccion)

2 . [Análisis de la vulnerabilidad](#analisis)

3 . [Escenarios actuales](#escenarios)

4 . [Practica](#practica)

5 . [Mitigación](#mitigacion)





## 1 . Introducción<a name="introduccion"></a>

Un ataque de falsificación de solicitudes del lado del servidor (ServerSideRequestForguery), se basa en que el atacante puede modificar una URL de una solicitud legitima y lanzar consultas que sean ejecutadas en el servidor.





## 2 . Análisis de la vulnerabilidad<a name="analisis"></a>

Este tipo de solicitudes serian ejecutadas en el servidor y esta petición pasaría a ser una solicitud interna del mismo servidor, pudiendo acceder a recursos que solo se pueden consultar desde la red interna, por ejemplo leer la configuración de metadatos de AWS, conectarse a servicios internos como bases de datos habilitadas para http o realizar solicitudes de publicación hacia servicios internos que no están destinados a estar expuestos.





## 3 . Escenarios actuales<a name="escenarios"></a>

Un escenario actual puede ser la obtención de metadatos de AWS con este método, dado que si no esta bien configurado se puede llegar a lanzar consultas a la API interna.

Otro escenario es un ataque de denegación de servicio, pero en vez de atacar al servidor principal que esta mas protegido, atacar a un servidor interno, saturando de este modo un servicio del que depende la web y provocando su mal funcionamiento o hasta la paralizacion de la misma.

Otro escenario podría ser el acceso a datos o plataformas que solo son accesibles desde la red interna como por ejemplo el acceso a un panel de administracion que esta protegido para que solo se pueda acceder desde la misma red.





## 4 . Practica<a name="practica"></a>


[![Video de la practica](https://img.youtube.com/vi/CaO5sSg9GpA/0.jpg)](https://www.youtube.com/watch?v=CaO5sSg9GpA)





## 5 . Mitigación<a name="mitigacion"></a>

Como medida de mitigación se debería prohibir en el codigo las peticiones que no sean http o https, asi como los accesos a redes privadas en las URL, también usar whitelist con los dominios aceptados y el uso de expresiones regulares que solo permitan lo que nuestra aplicación necesita.

Como en cualquier vulnerabilidad, también es muy importante tener los sistemas y programas actualizados, asi como tener politicas de seguridad que contemplen estos escenarios.







