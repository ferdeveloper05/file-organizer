from pathlib import Path


class ReglaOrganizador:
     
    def __init__(self, nombre_categoria: str, extensiones: list[str]):
        self.nombre_categoria = nombre_categoria
        self.extensiones = self._normalizar_extencion(extensiones)
        
    def _normalizar_extencion(self, extencion: list[str]) -> set: 
        extensiones_limpias = set()
        
        for exten in extencion: 
            ext = exten.lower()
            if not ext.startswith('.'): 
                ext = "."+ext
            extensiones_limpias.add(ext)
        
        return extensiones_limpias
    
    
    def coincide(self, path_dir: Path) -> bool: 
        extension_archivo = path_dir.suffix
        
        return extension_archivo in self.extensiones
    
    def __str__(self):
        return f"{self.nombre_categoria} = {self.extensiones}"
    
exten = [".pdf", "docx", ".txt"]

regla = ReglaOrganizador("Documento", exten)

print(regla.coincide(Path('archi.txt')))