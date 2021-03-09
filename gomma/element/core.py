
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Element SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "2.2.1"
__date__ = "2021-03-09"

import logging

from gomma.session import Session


class Element(object):
    """
    Element core class .
    """

    def __init__(self, profile_name=None):
        """
        Init Element cls.
        """
        logging.info(f'Init Element SDK -p {profile_name}')
        s = Session(profile_name)
        host = s.config.get('agapi_host')
        self.host = f'{host}/element'
        self.s = s

    # item
    def getItem(self, item_id: int, params={}):
        """
        Legge un item dal suo id.
        """
        logging.info(f'Get item {item_id}')
        rq = f'{self.host}/item/{item_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getItems(self, params={}):
        """
        Prende tutti gli items.
        """
        logging.info('Getting all the items')
        rq = f'{self.host}/item'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createItem(self, payload):
        """
        Create new item.
        """
        logging.info(f'Creating item {payload}')
        rq = f'{self.host}/item'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getItemFromErp(self, erp_id: int, erp_code: str, params={}):
        """
        Get item from erp.
        """
        logging.info(f'Search item from erp {erp_id} code {erp_code}.')
        query = {
            'erp': erp_id,
            'code': erp_code
        }
        payload = {**params, **query}
        rq = f'{self.host}/item/findByErp'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getItemFromCode(self, item_code: str, params={}):
        """
        Get item from code
        """
        logging.info(f'Search item code {item_code}.')
        query = {
            'code': item_code
        }
        payload = {**params, **query}
        rq = f'{self.host}/item/findByCode'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def attachItemErp(self, item_id: int, payload):
        """
        Attach Item Erp references.
        """
        logging.info(f'Attaching item {item_id} erp with {payload}')
        rq = f'{self.host}/item/{item_id}/erp'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateItem(self, item_id: int, payload):
        """
        Update item.
        """
        logging.info(f'Updating item {item_id} with {payload}')
        rq = f'{self.host}/item/{item_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def patchItem(self, item_id: int, payload):
        """
        Patch know item field.
        """
        logging.info(f'Patching item {item_id} with {payload}')
        rq = f'{self.host}/item/{item_id}'
        try:
            agent = self.s.getAgent()
            r = agent.patch(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def ItemAddAttribute(self, item_id: int, payload):
        """
        Create new item attributes.
        """
        logging.info(f'Creating item {item_id} attributes {payload}')
        rq = f'{self.host}/item/{item_id}/attribute'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def itemPatchAttribute(self, item_id: int, attribute_id: int, payload):
        """
        Patch item attribute.
        """
        logging.info(
            f'Patch item {item_id} attribute {attribute_id}-{payload}')
        rq = f'{self.host}/item/{item_id}/attribute/{attribute_id}'
        try:
            agent = self.s.getAgent()
            r = agent.patch(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def syncItemNorm(self, item_id: int, payload):
        """
        Sync item norm.
        """
        logging.info(f'Sync item {item_id} norm {payload}')
        rq = f'{self.host}/item/{item_id}/norm'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def itemAddCad(self, item_id: int, localFile):
        """ 
        Aggiunge un file cad all'item. 
        """
        logging.info(f'Add {localFile} to {item_id}')
        rq = f'{self.host}/item/{item_id}/cad'
        fin = open(localFile, 'rb')
        files = {'src': fin}
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, files=files)
        except Exception:
            logging.error(f'Failed request {rq} with files {files}')
            return False
        return self.s.response(r)

    def itemDeleteCad(self, item_id: int, cad_id: int):
        """ 
        Elimina un file cad dall'item. 
        """
        logging.info(f'Deleting cad {cad_id} at item {item_id}')
        rq = f'{self.host}/item/{item_id}/cad/{cad_id}'
        try:
            agent = self.s.getAgent()
            r = agent.delete(rq)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def itemAddCompetitor(self, item_id: int, payload):
        """ attach competitor to the item"""
        logging.info(f'Add xref item {item_id} {payload}')
        rq = f'{self.host}/item/{item_id}/competitor'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def itemUpdateCompetitor(self, item_id: int, xref_id: int, code: str):
        """ update item competitor cross reference"""
        logging.info(f'Update competitor {xref_id} with code {code}')
        payload = {
            'code': code
        }
        rq = f'{self.host}/item/{item_id}/competitor/{xref_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def itemDeleteCompetitor(self, item_id: int, competitor_id: int):
        """ Remove item competitor cross reference"""
        logging.info(
            f'Removing competitor {competitor_id} xref from item {item_id}')
        rq = f'{self.host}/item/{item_id}/competitor/{competitor_id}'
        try:
            agent = self.s.getAgent()
            r = agent.delete(rq)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # attribute
    def createAttribute(self, payload):
        """ crea un nuovo attributo """
        logging.info(f'Creating new attribute {payload}')
        rq = f'{self.host}/attribute'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getAttributes(self, params={}):
        """
        Read all attributes.
        """
        logging.info('Getting all the attributes.')
        rq = f'{self.host}/attribute'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getAttribute(self, attribute_id: int, params={}):
        """ Attribute by id """
        logging.info(f'Get attribute {attribute_id}')
        rq = f'{self.host}/attribute/{attribute_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getAttributeByName(self, attribute_name: str, params={}):
        """ Attribute by name """
        logging.info(f'Get attribute by name {attribute_name}')
        query = {
            'name': attribute_name
        }
        payload = {**params, **query}
        rq = f'{self.host}/attribute/findByName'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateAttribute(self, attribute_id: int, payload):
        """
        Update attribute.
        """
        logging.info(f'Updating attribute {attribute_id} ...')
        rq = f'{self.host}/attribute/{attribute_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # family
    def createFamily(self, payload):
        """ crea una nuova famiglia """
        logging.info(f'Creating new family {payload}')
        rq = f'{self.host}/family'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getFamilies(self, params={}):
        """
        Prende tutte le famiglie.
        """
        logging.info(f'Getting all the families with params {params}')
        rq = f'{self.host}/family'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getFamily(self, family_id: int, params={}):
        """
        Legge la singola famiglia.
        """
        logging.info(f'Reading family {family_id}')
        rq = f'{self.host}/family/{family_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateFamily(self, family_id: int, payload):
        """
        Update family.
        """
        logging.info(f'Updating family {family_id} with {payload}')
        rq = f'{self.host}/family/{family_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getFamilyFromCode(self, family_code: str, params={}):
        """ Prende famiglia da nome """
        logging.info(f'Get family from code {family_code} with {params}')
        query = {
            'code': family_code
        }
        payload = {**params, **query}
        rq = f'{self.host}/family/findByCode'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getFamilyAttributes(self, family_id: int, params={}):
        """ Read family attributes """
        logging.debug(f'getFamilyAttributes {family_id} with params {params}')
        rq = f'{self.host}/family/{family_id}/attribute'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def patchFamily(self, family_id: int, payload):
        """
        Patch family data.
        """
        logging.info(f'Patching family {family_id} with {payload}')
        rq = f'{self.host}/family/{family_id}'
        try:
            agent = self.s.getAgent()
            r = agent.patch(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def patchFamilyCategory(self, family_id: int, category_id: int):
        """
        Associa categoria a famiglia
        """
        logging.info(
            f'Patching family {family_id} with category {category_id}')
        rq = f'{self.host}/family/{family_id}'
        payload = {
            'category_id': category_id
        }
        try:
            agent = self.s.getAgent()
            r = agent.patch(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateFamilyCover(self, family_id: int, localFile):
        """ 
        Aggiorna cover famiglia. 
        """
        logging.info(f'Update family {family_id} cover with file {localFile}')
        rq = f'{self.host}/family/{family_id}/cover'
        fin = open(localFile, 'rb')
        files = {'src': fin}
        #files = {'src': ('test.cad', open(filepath, 'rb'), 'image/png')}
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, files=files)
        except Exception:
            logging.error(f'Failed request {rq} with files {files}')
            return False
        return self.s.response(r)

    def updateFamilyHq(self, family_id: int, localFile):
        """ 
        Aggiorna HQ famiglia. 
        """
        logging.info(f'Update family {family_id} hq with file {localFile}')
        rq = f'{self.host}/family/{family_id}/hq'
        fin = open(localFile, 'rb')
        files = {'src': fin}
        #files = {'src': ('test.cad', open(filepath, 'rb'), 'image/png')}
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, files=files)
        except Exception:
            logging.error(f'Failed request {rq} with files {files}')
            return False
        return self.s.response(r)

    def attachFamilyNorm(self, family_id: int, norm_id: int):
        """
        Aggiunge una norma riconosciuta, alla famiglia.
        SUGGEST - USE syncFamilyNorm!
        """
        logging.info(f'Attaching norm {norm_id} at family {family_id} ...')
        rq = f"{self.host}/family/{family_id}/norm"
        payload = {
            'norm_id': norm_id
        }
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def attachFamilyQuality(self, family_id: int, quality_id: int):
        """
        Aggiunge una qualità alla famiglia
        SUGGEST - USE syncFamilyNorm!
        """
        logging.info(f'Attach quality {quality_id} at family {family_id}')
        rq = f'{self.host}/family/{family_id}/quality'
        payload = {
            'quality_id': quality_id
        }
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def attachFamilyFeature(self, family_id: int, feature_id: int, description: str):
        """
        Aggiunge una feature alla famiglia.
        """
        logging.info(
            f'Attaching feature {feature_id} at family {family_id} with description {description}')
        payload = {
            'feature_id': feature_id,
            'description': description
        }
        rq = f'{self.host}/family/{family_id}/feature'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def attachFamilyAttribute(self, family_id: int, attribute_id: int):
        """
        Add attribute to family.
        """
        logging.info(
            f'Attaching attribute {attribute_id} to family {family_id}...')
        rq = f'{self.host}/family/{family_id}/attribute'
        payload = {
            'attribute_id': attribute_id
        }
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def attachFamilySorting(self, family_id: int, attribute_id: int):
        """
        Add attribute to sorting
        """
        logging.info(
            f'Attaching attribute {attribute_id} to family {family_id} sorting...')
        rq = f'{self.host}/family/{family_id}/sorting'
        payload = {
            'attribute_id': attribute_id
        }
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # feature
    def createFeature(self, feature_name: str):
        """
        Crea una nuova feature.
        """
        logging.info(f'Creating new feature with name {feature_name}')
        rq = f'{self.host}/feature'
        payload = {
            'name': feature_name
        }
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getFeatureByName(self, feature_name: str, params={}):
        """
        Prende feature dal nome.
        """
        logging.info(f'Getting feature by name {feature_name}...')
        query = {
            'name': feature_name
        }
        payload = {**params, **query}
        rq = f'{self.host}/feature/findByName'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # hub
    def getHubByName(self, hub_name: str):
        """ 
        Get hub from name
        """
        logging.info(f'Search hub by name {hub_name}')
        rq = f'{self.host}/hub/findByName?name={hub_name}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createHub(self, payload):
        """ 
        Create new hub
        """
        logging.info(f'Creating new hub {payload}')
        rq = f'{self.host}/hub'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # category
    def createCategory(self, hub_id: int, payload):
        """
        Crea un categoria.
        """
        logging.info(f'Creating new hub {hub_id} category with {payload}')
        rq = f'{self.host}/hub/{hub_id}/category'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getCategoryByName(self, hub_id: int, category_name: str):
        """
        Prende categoria da nome.
        """
        logging.info(f'Find category by name {category_name}')
        rq = f'{self.host}/hub/{hub_id}/category/findByName'
        payload = {
            'name': category_name
        }
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateCategoryCover(self, hub_id:int, category_id: int, localFile):
        """
        Aggiorna cover categoria.
        """
        logging.info(f'Update hub {hub_id} category {category_id} cover {localFile}')
        rq = f'{self.host}/hub/{hub_id}/category/{category_id}/cover'
        fin = open(localFile, 'rb')
        files = {'src': fin}
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, files=files)
        except Exception:
            logging.error(f'Failed request {rq} with files {files}')
            return False
        return self.s.response(r)

    # catalog
    def listCatalog(self, params={}):
        """ Get catalog by ID """
        logging.info(f'List catalogs {params}')
        rq = f'{self.host}/catalog'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getCatalog(self, catalog_id: int, params={}):
        """ Get catalog by ID """
        logging.info(f'Get catalog {catalog_id} with params {params}')
        rq = f'{self.host}/catalog/{catalog_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getTree(self, catalog_id: int, tree_id: int, params={}):
        """ Get catalog tree by ID """
        logging.info(f'Get catalog tree {catalog_id}')
        rq = f'{self.host}/catalog/{catalog_id}/tree/{tree_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getTreeLeaves(self, catalog_id: int, tree_id: int, params={}):
        """ Get catalog tree leaves """
        logging.info(f'Get catalog tree {tree_id} into catalog {catalog_id}')
        rq = f'{self.host}/catalog/{catalog_id}/tree/{tree_id}/leaf'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getTreeLeaf(self, catalog_id: int, tree_id: int, leaf_id: int, params={}):
        """ Get catalog tree leaf ID """
        logging.info(f'Get catalog tree {catalog_id}')
        rq = f'{self.host}/catalog/{catalog_id}/tree/{tree_id}/leaf/{leaf_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)
