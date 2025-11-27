class Graph:
    def __init__(self):
        """Инициализация неориентированного графа"""
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """Добавление вершины в граф"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Добавление ребра между vertex1 и vertex2"""
        # Добавляем вершины, если их еще нет
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Добавляем двусторонние связи для графа
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    def dfs(self, start_vertex=None):
        """
        Обход графа в глубину(DFS)

            start_vertex: Начальная вершина. Если None, берется первая вершина

            Возвращает список посещенных вершин в порядке обхода
        """
        if not self.adjacency_list:
            return []

        # Если начальная вершина не указана, берем первую
        if start_vertex is None:
            start_vertex = next(iter(self.adjacency_list))

        # Проверяем, что начальная вершина существует
        if start_vertex not in self.adjacency_list:
            raise ValueError(f"Вершина {start_vertex} не существует в графе")

        visited = []
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                # Добавляем соседей в стек в обратном порядке
                # для сохранения естественного порядка обхода
                for neighbor in reversed(self.adjacency_list[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited

    def dfs_recursive(self, start_vertex=None):
        """
        Рекурсивная версия обхода в глубину

            start_vertex: Начальная вершина. Если None, берется первая вершина

            Возвращает список посещенных вершин в порядке обхода
        """
        if not self.adjacency_list:
            return []

        if start_vertex is None:
            start_vertex = next(iter(self.adjacency_list))

        if start_vertex not in self.adjacency_list:
            raise ValueError(f"Вершина {start_vertex} не существует в графе")

        visited = []

        def _dfs_recursive(vertex):
            visited.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    _dfs_recursive(neighbor)

        _dfs_recursive(start_vertex)
        return visited

    def __iter__(self):
        """Делает граф итерируемым (используется DFS для порядка обхода)"""
        self._dfs_order = self.dfs()
        self._index = 0
        return self

    def __next__(self):
        """Возвращает следующую вершину при итерации"""
        if self._index < len(self._dfs_order):
            vertex = self._dfs_order[self._index]
            self._index += 1
            return vertex
        raise StopIteration

    def __str__(self):
        """Строковое представление графа"""
        result = []
        for vertex, neighbors in self.adjacency_list.items():
            result.append(f"{vertex}: {neighbors}")
        return "\n".join(result)

    def __contains__(self, vertex):
        """Проверка наличия вершины в графе"""
        return vertex in self.adjacency_list

    def get_vertices(self):
        """Возвращает список всех вершин графа"""
        return list(self.adjacency_list.keys())

    def get_edges(self):
        """Возвращает список всех ребер графа"""
        edges = set()
        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                # Храним ребра без дубликатов
                edge = tuple(sorted((vertex, neighbor)))
                edges.add(edge)
        return list(edges)

