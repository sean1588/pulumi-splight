# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ComponentArgs', 'Component']

@pulumi.input_type
class ComponentArgs:
    def __init__(__self__, *,
                 inputs: pulumi.Input[Sequence[pulumi.Input['ComponentInputArgs']]],
                 version: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Component resource.
        :param pulumi.Input[Sequence[pulumi.Input['ComponentInputArgs']]] inputs: The input parameters based on hubcomponent spec
        :param pulumi.Input[str] version: [NAME-VERSION] the version of the hub component
        :param pulumi.Input[str] description: optinal description to add details of the resource
        :param pulumi.Input[str] name: the name of the component to be created
        """
        pulumi.set(__self__, "inputs", inputs)
        pulumi.set(__self__, "version", version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def inputs(self) -> pulumi.Input[Sequence[pulumi.Input['ComponentInputArgs']]]:
        """
        The input parameters based on hubcomponent spec
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: pulumi.Input[Sequence[pulumi.Input['ComponentInputArgs']]]):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        [NAME-VERSION] the version of the hub component
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        optinal description to add details of the resource
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        the name of the component to be created
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ComponentState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 inputs: Optional[pulumi.Input[Sequence[pulumi.Input['ComponentInputArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Component resources.
        :param pulumi.Input[str] description: optinal description to add details of the resource
        :param pulumi.Input[Sequence[pulumi.Input['ComponentInputArgs']]] inputs: The input parameters based on hubcomponent spec
        :param pulumi.Input[str] name: the name of the component to be created
        :param pulumi.Input[str] version: [NAME-VERSION] the version of the hub component
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if inputs is not None:
            pulumi.set(__self__, "inputs", inputs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        optinal description to add details of the resource
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ComponentInputArgs']]]]:
        """
        The input parameters based on hubcomponent spec
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ComponentInputArgs']]]]):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        the name of the component to be created
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        [NAME-VERSION] the version of the hub component
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Component(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 inputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentInputArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import json
        import pulumi_splight as splight

        component_test = splight.Component("componentTest",
            description="Created with Terraform",
            version="Random-3.1.0",
            inputs=[
                splight.ComponentInputArgs(
                    name="period",
                    type="int",
                    value=json.dumps(10),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
                splight.ComponentInputArgs(
                    name="min",
                    type="int",
                    value=json.dumps(1),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
                splight.ComponentInputArgs(
                    name="max",
                    type="int",
                    value=json.dumps(150),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
                splight.ComponentInputArgs(
                    name="max_iterations",
                    type="int",
                    value=json.dumps(3),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
                splight.ComponentInputArgs(
                    name="should_crash",
                    type="bool",
                    value=json.dumps("true"),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import splight:index/component:Component [options] splight_component.<name> <component_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: optinal description to add details of the resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentInputArgs']]]] inputs: The input parameters based on hubcomponent spec
        :param pulumi.Input[str] name: the name of the component to be created
        :param pulumi.Input[str] version: [NAME-VERSION] the version of the hub component
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComponentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import json
        import pulumi_splight as splight

        component_test = splight.Component("componentTest",
            description="Created with Terraform",
            version="Random-3.1.0",
            inputs=[
                splight.ComponentInputArgs(
                    name="period",
                    type="int",
                    value=json.dumps(10),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
                splight.ComponentInputArgs(
                    name="min",
                    type="int",
                    value=json.dumps(1),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
                splight.ComponentInputArgs(
                    name="max",
                    type="int",
                    value=json.dumps(150),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
                splight.ComponentInputArgs(
                    name="max_iterations",
                    type="int",
                    value=json.dumps(3),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
                splight.ComponentInputArgs(
                    name="should_crash",
                    type="bool",
                    value=json.dumps("true"),
                    multiple=False,
                    required=False,
                    sensitive=False,
                    description="",
                ),
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import splight:index/component:Component [options] splight_component.<name> <component_id>
        ```

        :param str resource_name: The name of the resource.
        :param ComponentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComponentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 inputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentInputArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ComponentArgs.__new__(ComponentArgs)

            __props__.__dict__["description"] = description
            if inputs is None and not opts.urn:
                raise TypeError("Missing required property 'inputs'")
            __props__.__dict__["inputs"] = inputs
            __props__.__dict__["name"] = name
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
        super(Component, __self__).__init__(
            'splight:index/component:Component',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            inputs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentInputArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'Component':
        """
        Get an existing Component resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: optinal description to add details of the resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ComponentInputArgs']]]] inputs: The input parameters based on hubcomponent spec
        :param pulumi.Input[str] name: the name of the component to be created
        :param pulumi.Input[str] version: [NAME-VERSION] the version of the hub component
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ComponentState.__new__(_ComponentState)

        __props__.__dict__["description"] = description
        __props__.__dict__["inputs"] = inputs
        __props__.__dict__["name"] = name
        __props__.__dict__["version"] = version
        return Component(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        optinal description to add details of the resource
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def inputs(self) -> pulumi.Output[Sequence['outputs.ComponentInput']]:
        """
        The input parameters based on hubcomponent spec
        """
        return pulumi.get(self, "inputs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        the name of the component to be created
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        [NAME-VERSION] the version of the hub component
        """
        return pulumi.get(self, "version")

