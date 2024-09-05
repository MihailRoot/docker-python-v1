import requests
from typing import Optional, Dict, List, Any, Literal
import json
import asyncio

class Docker():
    
    def __init__(self, server) -> None:
        self.server = server

    #Get_all containers with filters
    #filter will be later
    def get_container(self, getall: Optional[bool] = False ) -> Optional[List[Dict[str, Any]]]:
        """
    Create a new container with the given configuration.

    Args:
        getall(Bool): Get all containers(It replaced cause python have 'all')
    
    Returns: 
        Dict[str, Any]: Information about the created container.

    Raises:
        requests.RequestException: If there's an error in the API request.
    """
        try:

            params = {"all":True if getall else 'false'}
            get_all = requests.get(f'http://{self.server}/v1.46/containers/json',headers={'Content-Type':"application/json"}, params=params)
            return get_all.json()
        
        except requests.RequestException:
            return []
    
    def create(self,data:Dict[str,Any]  ) -> Dict[str,Any]:
        
        try:
            
            create = requests.post(f'http://{self.server}/v1.46/containers/create',headers={'Content-Type':"application/json"}, data=json.dumps(data))
            container = create.json()
            container['status_code'] = create.status_code
            print(container["Id"])
            data1 = {
                "id":container['Id']
            }
            runcontainer =  requests.post(f'http://{self.server}/v1.46/containers/{container["Id"]}/start', headers={'Content-Type':"application/json"} )
            container['start'] = runcontainer.status_code
            return  container
        
        except requests.RequestException:
            return {}
    
    
    def logs(self,id: int, follow: bool = False, stdout: bool = False, 
             stderr: bool = False, since: int = 0, until: int = 0, timestamps: bool = False, tail: str = 'all' ): # Логирование контейнера
        """
        Получает логи контейнера.

        :param id: ID контейнера.
        :param follow: Если True, будет следить за логами.
        :param stdout: Если True, возвращает стандартный вывод.
        :param stderr: Если True, возвращает стандартный вывод ошибок.
        :param since: Возвращает логи с указанного времени.
        :param until: Возвращает логи до указанного времени.
        :param timestamps: Если True, добавляет временные метки к логам.
        :param tail: Количество последних строк логов, которые нужно вернуть.
        :return: Логи контейнера в виде словаря.
        """
        try:
            params = {
               'follow':follow,
               'stdout': stdout,
               'stderr':stderr,
               'since':since,
               'until':until,
               'timestamps': timestamps,
               'tail': tail, 
            }
            response = requests.get(f'http://{self.server}/v1.46/containers/{id}/logs',headers={'Content-Type':"application/json"}, params=params) 
            logs = response.content.decode('utf-8')
            return logs
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}
        
    def info(self, id:int, size: Optional[bool] = False) -> Optional[List[Dict[str, Any]]]:
        """
        Получает логи контейнера.

        :param id: ID контейнера.
        :param size: Если True, возвращает размер контейнера в полях SizeRw и SizeRootFs.
        :return: Логи контейнера в виде словаря.
        """
        try:
            get_info = requests.get(f'http://{self.server}/v1.46/containers/{id}/json', headers={'Content-Type':"application/json"})
        
            return get_info.json()
        
        except ValueError as ve:
            print(ve)
            return []
        
        except requests.exceptions.RequestException as e:
            print(e)
            return []
    def remove(self, id: int ): # Логирование контейнера
        try:
            response = requests.delete(f'http://{self.server}/v1.46/containers/{id}',headers={'Content-Type':"application/json"}) 
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}
    
    def restart(self, id: int ): # Логирование контейнера
        try:
            response = requests.post(f'http://{self.server}/v1.46/containers/{id}/restart',headers={'Content-Type':"application/json"}) 
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}
        
    def kill(self, id: int ): # Логирование контейнера
        try:
            response = requests.post(f'http://{self.server}/v1.46/containers/{id}/kill',headers={'Content-Type':"application/json"}) 
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}
    def update(self, id:int, data: Dict[str, Any] ): # Логирование контейнера
        try:
            response = requests.post(f'http://{self.server}/v1.46/containers/{id}',headers={'Content-Type':"application/json"}, data=data) 
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}
    def rename(self, id:int, name:Any ): # Логирование контейнера
        try:
            data = {
                'name': name
            }
            response = requests.post(f'http://{self.server}/v1.46/containers/{id}/rename',headers={'Content-Type':"application/json"}, data=data) 
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}   
    def pause(self, id:int ): # Логирование контейнера
        try:

            response = requests.post(f'http://{self.server}/v1.46/containers/{id}/pause',headers={'Content-Type':"application/json"}) 
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}   
    def unpause(self, id:int ): # Логирование контейнера
        try:

            response = requests.post(f'http://{self.server}/v1.46/containers/{id}/unpause',headers={'Content-Type':"application/json"}) 
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching logs: {e}")
            return {}
        except ValueError as ve:
            print(ve)
            return {}   
        
test = Docker("localhost:2375")
container = test.create({'Image':'ubuntu','cmd':["/bin/sh", "-c", "apt update -y  && apt install -y nginx"],'tty': True, 'stdin_open':True})
