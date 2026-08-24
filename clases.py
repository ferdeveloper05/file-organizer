from pathlib import Path


class ReglaOrganizador:
     
    def __init__(self, nombre_categoria: str, extensiones: list[str]):
        self.nombre_categoria = nombre_categoria
        self._extensiones = extensiones
    
    
    def coincide(self, path_dir: Path) -> bool: 
        pass
    
    def __str__(self):
        return f"{self.nombre_categoria} = {self.extensiones}"
    
exten = [".pdf", "docx", ".txt"]

regla = ReglaOrganizador("Documento", exten)

print(regla)